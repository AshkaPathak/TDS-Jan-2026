# GA4 — Q4: dbt Operations Performance Mart (Daily FCR Model)

## Problem Summary

Orbit Ops uses **dbt** to power operational dashboards for support leadership.  
This mart model delivers **First Contact Resolution (FCR)** and SLA metrics at a **daily grain** for the last 14 days.

The model:

- Uses `{{ config() }}` for materialization and metadata
- References upstream models via `{{ ref() }}`
- Filters to a rolling 14-day window
- Aggregates metrics at daily grain per contact channel
- Computes SLA breach logic and FCR rates
- Handles NULLs appropriately
- Returns BI-ready columns ordered by date

---

## Model Details

**Model Name**  
`models/marts/fct_daily_first_contact_resolution.sql`

**Grain**  
One row per `(contact_date × contact_channel)`

**Window**  
Rolling 14 days relative to `current_date`

**Downstream**  
Support Operations Dashboard — FCR Trend

---

## Final dbt Mart Model

```sql
-- =============================================================================
-- models/marts/fct_daily_first_contact_resolution.sql
--
-- Purpose : Powers the Orbit Ops support dashboard for operational leaders.
--           Delivers first-contact resolution (FCR) metrics at daily grain
--           for a rolling 14-day window.
--
-- Grain   : One row per contact_channel per calendar day.
-- Upstream: int_support_contacts, stg_tickets, stg_sla_targets,
--           stg_shipments, stg_returns
-- Downstream: BI dashboard — "Support Operations / FCR Trend"
--
-- Refresh : Scheduled daily at 06:00 UTC (after upstream staging runs).
-- =============================================================================

{{
    config(
        materialized   = 'table',
        tags           = ['marts', 'support', 'daily'],
        meta           = {
            'owner'          : 'support-analytics@orbitops.com',
            'sla_sensitivity': 'high',
            'freshness_warn_after' : {'hours': 25},
            'freshness_error_after': {'hours': 49}
        }
    )
}}

with

tickets as (
    select * from {{ ref('stg_tickets') }}
),

sla_targets as (
    select * from {{ ref('stg_sla_targets') }}
),

shipments as (
    select * from {{ ref('stg_shipments') }}
),

returns as (
    select * from {{ ref('stg_returns') }}
),

recent_tickets as (
    select *
    from tickets
    where
        cast(opened_at as date) >= current_date - 14
        and ticket_type not in ('test', 'spam', 'internal')
        and is_deleted = false
),

enriched_tickets as (
    select
        t.ticket_id,
        t.customer_id,
        t.opened_at,
        t.resolved_at,
        t.contact_channel,
        t.agent_id,
        t.ticket_priority,
        t.is_first_contact_resolved,
        t.reopened_count,
        t.csat_score,
        t.first_response_at,

        datediff('minute', t.opened_at, t.resolved_at) as resolution_minutes,
        datediff('minute', t.opened_at, t.first_response_at) as first_response_minutes,

        case when s.shipment_id is not null then true else false end as has_linked_shipment,
        case when r.return_id is not null then true else false end as has_linked_return

    from recent_tickets t
    left join shipments s on t.reference_id = s.shipment_id
    left join returns r on t.reference_id = r.return_id
),

sla_evaluated as (
    select
        e.*,

        case
            when e.is_first_contact_resolved = true
             and e.reopened_count = 0 then true
            else false
        end as is_true_fcr,

        case
            when e.first_response_minutes
                 > coalesce(sl.response_sla_minutes, 1440) then true
            else false
        end as is_response_sla_breached,

        case
            when coalesce(e.resolution_minutes, 99999)
                 > coalesce(sl.resolution_sla_hours, 48) * 60 then true
            else false
        end as is_resolution_sla_breached,

        coalesce(sl.fcr_target_pct, 0.80)       as fcr_sla_target_pct,
        coalesce(sl.response_sla_minutes, 1440) as response_sla_minutes,
        coalesce(sl.resolution_sla_hours, 48)   as resolution_sla_hours

    from enriched_tickets e
    left join sla_targets sl using (contact_channel)
),

daily_aggregated as (
    select
        date_trunc('day', opened_at) as contact_date,
        contact_channel,

        count(ticket_id) as total_contacts,
        count(case when has_linked_shipment then 1 end) as contacts_with_shipment,
        count(case when has_linked_return then 1 end) as contacts_with_return,
        count(case when resolved_at is not null then 1 end) as resolved_contacts,

        count(case when is_true_fcr then 1 end) as fcr_count,

        avg(case when resolved_at is not null then resolution_minutes end)
            as avg_resolution_minutes,

        avg(first_response_minutes) as avg_first_response_minutes,

        count(case when is_response_sla_breached then 1 end)
            as response_sla_breaches,

        count(case when is_resolution_sla_breached then 1 end)
            as resolution_sla_breaches,

        avg(csat_score) as avg_csat_score,
        count(csat_score) as csat_response_count,

        count(case when ticket_priority = 'critical' then 1 end)
            as critical_contacts,

        count(case when ticket_priority = 'high' then 1 end)
            as high_contacts,

        max(fcr_sla_target_pct) as fcr_sla_target_pct,
        max(response_sla_minutes) as response_sla_minutes_target,
        max(resolution_sla_hours) as resolution_sla_hours_target

    from sla_evaluated
    group by 1, 2
),

final as (
    select
        {{ dbt_utils.generate_surrogate_key(['contact_date', 'contact_channel']) }}
            as daily_fcr_id,

        contact_date,
        contact_channel,

        coalesce(total_contacts, 0) as total_contacts,
        coalesce(resolved_contacts, 0) as resolved_contacts,
        coalesce(contacts_with_shipment, 0) as contacts_with_shipment,
        coalesce(contacts_with_return, 0) as contacts_with_return,
        coalesce(critical_contacts, 0) as critical_contacts,
        coalesce(high_contacts, 0) as high_contacts,

        coalesce(fcr_count, 0) as fcr_count,

        round(
            case when total_contacts > 0
                 then fcr_count / total_contacts
                 else null
            end,
        4) as fcr_rate,

        fcr_sla_target_pct,
        response_sla_minutes_target,
        resolution_sla_hours_target,

        case
            when total_contacts = 0 then null
            when (fcr_count / total_contacts) >= fcr_sla_target_pct then 'met'
            else 'missed'
        end as fcr_sla_status,

        coalesce(response_sla_breaches, 0) as response_sla_breaches,
        coalesce(resolution_sla_breaches, 0) as resolution_sla_breaches,

        round(
            case when total_contacts > 0
                 then response_sla_breaches / total_contacts
                 else null
            end,
        4) as response_sla_breach_rate,

        round(
            case when total_contacts > 0
                 then resolution_sla_breaches / total_contacts
                 else null
            end,
        4) as resolution_sla_breach_rate,

        round(coalesce(avg_resolution_minutes, 0), 2)
            as avg_resolution_minutes,

        round(coalesce(avg_first_response_minutes, 0), 2)
            as avg_first_response_minutes,

        round(avg_csat_score, 2) as avg_csat_score,
        coalesce(csat_response_count, 0) as csat_response_count,

        current_timestamp as dbt_loaded_at

    from daily_aggregated
)

select * from final
order by contact_date desc, contact_channel
