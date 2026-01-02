from pydantic import BaseModel
from typing import List, Optional
# from datetime import date

class TimesheetEntry(BaseModel):
    day_of_month: int
    hours_worked: Optional[float] = 0
    remarks: Optional[str] = None

class Timesheet(BaseModel):
    employee_id: str
    start_year: int
    start_month: int
    entries: Optional[List[TimesheetEntry]] = []
