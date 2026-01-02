from fastapi.responses import StreamingResponse
from services.excel import generate_timesheet_excel

def export_timesheet_controller(data):

    out_file = generate_timesheet_excel(data)

    file_like = open(out_file, "rb")
    return StreamingResponse(
        file_like,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": f"attachment; filename=timesheet.xlsx"}
    )
