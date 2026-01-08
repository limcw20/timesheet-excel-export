from fastapi.responses import FileResponse
from services.excel import generate_timesheet_excel

def export_timesheet_controller(data):
    out_file = generate_timesheet_excel(data)

    return FileResponse(
        path=out_file,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename="timesheet.xlsx"
    )
