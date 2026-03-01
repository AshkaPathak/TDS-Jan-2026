import json
import re
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS: allow GET requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Regex patterns for the templated queries
RE_TICKET = re.compile(r"^What is the status of ticket (\d+)\?$")
RE_MEETING = re.compile(r"^Schedule a meeting on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)\.$")
RE_EXPENSE = re.compile(r"^Show my expense balance for employee (\d+)\.$")
RE_BONUS = re.compile(r"^Calculate performance bonus for employee (\d+) for (\d{4})\.$")
RE_ISSUE = re.compile(r"^Report office issue (\d+) for the (.+) department\.$")


def make_response(name: str, ordered_items: list[tuple[str, object]]):
    """
    IMPORTANT: arguments must preserve function signature order.
    We build dict from ordered key-value pairs and dump as JSON string.
    """
    arguments_str = json.dumps(dict(ordered_items), separators=(",", ":"))
    return {"name": name, "arguments": arguments_str}


@app.get("/execute")
def execute(q: str = Query(...)):
    q = q.strip()

    m = RE_TICKET.match(q)
    if m:
        ticket_id = int(m.group(1))
        return make_response("get_ticket_status", [("ticket_id", ticket_id)])

    m = RE_MEETING.match(q)
    if m:
        date = m.group(1)
        time_ = m.group(2)
        meeting_room = m.group(3).strip()
        return make_response(
            "schedule_meeting",
            [("date", date), ("time", time_), ("meeting_room", meeting_room)],
        )

    m = RE_EXPENSE.match(q)
    if m:
        employee_id = int(m.group(1))
        return make_response("get_expense_balance", [("employee_id", employee_id)])

    m = RE_BONUS.match(q)
    if m:
        employee_id = int(m.group(1))
        current_year = int(m.group(2))
        return make_response(
            "calculate_performance_bonus",
            [("employee_id", employee_id), ("current_year", current_year)],
        )

    m = RE_ISSUE.match(q)
    if m:
        issue_code = int(m.group(1))
        department = m.group(2).strip()
        return make_response(
            "report_office_issue",
            [("issue_code", issue_code), ("department", department)],
        )

    raise HTTPException(status_code=400, detail="Query does not match any known template")
