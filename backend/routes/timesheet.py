from fastapi import APIRouter
from controllers.timesheet import export_timesheet_controller
from models.timesheet import Timesheet

router = APIRouter()

@router.post("/export")
def export_timesheet(timesheet: Timesheet):
    data = timesheet.dict()
    return export_timesheet_controller(data)