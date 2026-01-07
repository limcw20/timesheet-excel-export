from pydantic import BaseModel
from typing import List, Optional
# from datetime import date

class TimesheetEntry(BaseModel):
    day_of_month: int
    time_in: Optional[str] = None
    time_out: Optional[str] = None
    hours_worked: Optional[float] = 0
    reason_for_absence: Optional[str] = None

class Timesheet(BaseModel):
    employee_id: str
    start_year: int
    start_month: int
    entries: Optional[List[TimesheetEntry]] = []
