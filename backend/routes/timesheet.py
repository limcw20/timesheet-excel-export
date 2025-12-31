from fastapi import APIRouter
from controllers.timesheet import export_timesheet_controller
from models.timesheet import Timesheet

router = APIRouter()

@router.post("/export")
def export_timesheet(timesheet: Timesheet):
    return export_timesheet_controller(timesheet)