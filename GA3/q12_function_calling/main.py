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
# More tolerant patterns (case-insensitive, flexible spaces, optional punctuation)
RE_TICKET = re.compile(r"(?i)^\s*What\s+is\s+the\s+status\s+of\s+ticket\s+(\d+)\s*\??\s*$")

RE_MEETING = re.compile(
    r"(?i)^\s*Schedule\s+a\s+meeting\s+on\s+(\d{4}-\d{2}-\d{2})\s+at\s+(\d{2}:\d{2})\s+in\s+(.+?)\s*\.?\s*$"
)

RE_EXPENSE = re.compile(r"(?i)^\s*Show\s+my\s+expense\s+balance\s+for\s+employee\s+(\d+)\s*\.?\s*$")

RE_BONUS = re.compile(
    r"(?i)^\s*Calculate\s+performance\s+bonus\s+for\s+employee\s+(\d+)\s+for\s+(\d{4})\s*\.?\s*$"
)

RE_ISSUE = re.compile(
    r"(?i)^\s*Report\s+office\s+issue\s+(\d+)\s+for\s+(?:the\s+)?(.+?)\s+department\s*\.?\s*$"
)

def make_response(name: str, ordered_items: list[tuple[str, object]]):
    """
    IMPORTANT: arguments must preserve function signature order.
    We build dict from ordered key-value pairs and dump as JSON string.
    """
    arguments_str = json.dumps(dict(ordered_items), separators=(",", ":"))
    return {"name": name, "arguments": arguments_str}


@app.get("/execute")
def execute(q: str | None = Query(None)):
    if not q:
        return {"name": "help", "arguments": "{}"}
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
