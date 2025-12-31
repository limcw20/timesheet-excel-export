from fastapi.responses import StreamingResponse
from services.excel import generate_timesheet_excel
from models.timesheet import Timesheet

def export_timesheet_controller(timesheet: Timesheet):

    data = timesheet.dict()
    out_file = generate_timesheet_excel(data)

    file_like = open(out_file, "rb")
    return StreamingResponse(
        file_like,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": f"attachment; filename=timesheet_{timesheet.employee_id}.xlsx"}
    )
