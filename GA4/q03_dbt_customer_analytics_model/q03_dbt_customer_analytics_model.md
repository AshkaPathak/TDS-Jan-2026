# GA4 — Q3: dbt Intermediate Model for GMV Trend Analysis

## Problem Summary

You are building customer analytics for a marketplace using **dbt**. The analytics team needs reliable, tested, and well-documented transformation logic to analyze **GMV (Gross Merchandise Value)** trends over time.

Your task is to write a **dbt intermediate model** that:
- Uses `{{ ref() }}` to reference upstream staging models
- Applies business logic suitable for GMV analysis
- Cleans and filters raw transactional data
- Performs intermediate transformations and joins
- Produces an analysis-ready output for downstream mart models

---

## Business Context

The company tracks GMV metrics and wants trend analysis over a recent rolling window. This model:
- Filters to **completed**, **non-deleted** transactions
- Restricts to a **recent rolling 90-day window**
- Enriches transactions with product metadata
- Aggregates volume at a weekly grain for trend comparisons
- Joins customer attributes for easy segmentation in BI

---

## Model Output Grain

One row per:

(customer × product_category × week_start_date)

This produces a clean intermediate dataset that downstream marts can further aggregate into daily/weekly/monthly dashboards as needed.

---

## Final dbt Intermediate Model (SQL)

Save as an intermediate model such as:

`models/intermediate/int_customer_gmv.sql`

```sql
with customers as (
    select * from {{ ref('stg_customers') }}
),

transactions as (
    select * from {{ ref('stg_transactions') }}
),

products as (
    select * from {{ ref('stg_products') }}
),

-- -------------------------------------------------------------------------
-- Filter to a rolling 90-day window for trend analysis.
-- We use dateadd/datediff compatible syntax; adjust for your warehouse dialect
-- (e.g., CURRENT_DATE - INTERVAL '90 days' for Postgres/Snowflake/BigQuery).
-- -------------------------------------------------------------------------
recent_transactions as (
    select *
    from transactions
    where
        transaction_date >= {{ dbt_utils.dateadd('day', -90, 'current_date') }}
        and transaction_status = 'completed'    -- exclude pending / reversed txns
        and is_deleted = false                  -- soft-delete guard
),

-- -------------------------------------------------------------------------
-- Enrich transactions with product metadata so we can segment by
-- product category in the volume aggregation below.
-- -------------------------------------------------------------------------
enriched_transactions as (
    select
        t.transaction_id,
        t.customer_id,
        t.transaction_date,
        t.transaction_amount,
        t.transaction_currency,

        -- Normalise to USD for cross-currency volume comparison.
        -- fx_rate is maintained daily in stg_transactions.
        t.transaction_amount * t.fx_rate_to_usd   as transaction_amount_usd,

        p.product_id,
        p.product_category,
        p.product_subcategory

    from recent_transactions     t
    left join products           p using (product_id)
),

-- -------------------------------------------------------------------------
-- Truncate each transaction date to the start of its ISO week (Monday).
-- This creates a consistent weekly spine regardless of which day a
-- transaction falls on, making week-over-week comparisons straightforward.
-- -------------------------------------------------------------------------
weekly_tagged as (
    select
        *,
        -- {{ dbt_utils.date_trunc('week', 'transaction_date') }} returns the
        -- Monday of the week containing transaction_date.
        {{ dbt_utils.date_trunc('week', 'transaction_date') }} as week_start_date
    from enriched_transactions
),

-- -------------------------------------------------------------------------
-- Core aggregation: one row per (customer × product_category × week).
-- Volume is measured by both count and USD amount to support dual-axis
-- dashboard charts (transaction count vs. dollar throughput).
-- -------------------------------------------------------------------------
weekly_volume as (
    select
        customer_id,
        product_category,
        week_start_date,

        -- Transaction count metrics
        count(transaction_id)                           as txn_count,
        count(distinct transaction_date)                as active_days_in_week,

        -- Value metrics (USD-normalised)
        sum(transaction_amount_usd)                     as total_volume_usd,
        avg(transaction_amount_usd)                     as avg_transaction_usd,
        min(transaction_amount_usd)                     as min_transaction_usd,
        max(transaction_amount_usd)                     as max_transaction_usd

    from weekly_tagged
    {{ dbt_utils.group_by(3) }}   -- groups by customer_id, product_category, week_start_date
),

-- -------------------------------------------------------------------------
-- Join customer attributes so downstream marts can filter/segment without
-- needing to re-join to the customers table themselves.
-- -------------------------------------------------------------------------
final as (
    select
        -- Surrogate key: stable identifier for this grain
        {{ dbt_utils.generate_surrogate_key([
            'wv.customer_id',
            'wv.product_category',
            'wv.week_start_date'
        ]) }}                                           as weekly_volume_id,

        -- Customer attributes
        c.customer_id,
        c.customer_name,
        c.customer_segment,     -- e.g. 'SMB', 'Enterprise', 'Consumer'
        c.customer_region,
        c.account_status,

        -- Time dimension
        wv.week_start_date,
        dateadd('day', 6, wv.week_start_date)          as week_end_date,

        -- Product dimension
        wv.product_category,

        -- Volume metrics
        wv.txn_count,
        wv.active_days_in_week,
        wv.total_volume_usd,
        wv.avg_transaction_usd,
        wv.min_transaction_usd,
        wv.max_transaction_usd,

        -- Derived flags used by the BI layer for conditional formatting
        case
            when wv.txn_count = 0    then 'inactive'
            when wv.txn_count < 5    then 'low'
            when wv.txn_count < 20   then 'medium'
            else                          'high'
        end                                             as activity_band,

        -- Metadata
        current_timestamp                               as dbt_loaded_at

    from weekly_volume      wv
    inner join customers    c using (customer_id)

    -- Exclude churned or internally-flagged test accounts from dashboards
    where c.account_status not in ('churned', 'test', 'internal')
)

select * from final
