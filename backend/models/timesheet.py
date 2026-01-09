from pydantic import BaseModel
from typing import List, Optional
# from datetime import date

class TimesheetEntry(BaseModel):
    day_of_month: int
    time_in: Optional[str] = "09:00am"
    time_out: Optional[str] = "06:00pm"
    hours_worked: Optional[float] = 8
    reason_for_absence: Optional[str] = None
    ot_from: Optional[str] = None
    ot_to: Optional[str] = None
    ot_hours: Optional[float] = 0
    ot_approved_by: Optional[str] = None

class Timesheet(BaseModel):
    start_year: int
    start_month: int
    entries: Optional[List[TimesheetEntry]] = []
