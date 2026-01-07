from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from datetime import datetime, timedelta
import uuid
import os

# Temporary directory (to change when all is done)
TMP_DIR = "tmp"
os.makedirs(TMP_DIR, exist_ok=True)

def generate_timesheet_excel(timesheet: dict) -> str:

    wb = Workbook()
    ws = wb.active

    bold_font = Font(bold=True)
    center_align = Alignment(horizontal="center")
    thin_border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )

    # 1st Row Title
    ws.merge_cells("A1:K1") 
    title_cell = ws["A1"] 
    title_cell.value = "Time Sheet" 
    title_cell.font = Font(bold=True, size=20) 
    title_cell.alignment = center_align

    # Headers
    headers = ["Date", "Weekday", "Reason for Absence", "Time In", "Time Out", "Hours Worked"]
    for col, header in enumerate(headers, start=1):
        cell = ws.cell(row=3, column=col, value=header) # Header at row n
        cell.font = bold_font
        cell.alignment = center_align
        cell.border = thin_border

    start_year = timesheet['start_year']
    start_month = timesheet['start_month']
    start_date = datetime(start_year, start_month, 4) # start from nth day of month

    if start_month == 12:
        next_year = start_year + 1
        next_month = 1
    else:
        next_year = start_year
        next_month = start_month + 1

    end_date = datetime(next_year, next_month, 3) # end at nth day of next month
    total_days = (end_date - start_date).days + 1

    entries = {e.get('day_of_month'): e for e in timesheet.get('entries', [])}

    for i in range(total_days):
        row_num = i + 4 # Data starts from row n
        date_obj = start_date + timedelta(days=i)
        weekday = date_obj.strftime("%A")
        day_of_month = date_obj.day

        # Extract payload data if exists
        if day_of_month in entries:
            entry = entries[day_of_month]
            hours_worked = entry.get('hours_worked', hours_worked)
            hours_worked = entry.get('time_in', time_in)
            hours_worked = entry.get('time_out', time_out)
            reason_for_absence = entry.get('reason_for_absence', reason_for_absence)

        # Default logic if weekends
        if weekday in ["Saturday", "Sunday"]:
            hours_worked = None
            reason_for_absence = ""
            time_in = None
            time_out = None
        
        # Logic for full day absent codes
        elif reason_for_absence in ["AL", "MC", "UPL"]:
            print("here")
            hours_worked = None
            reason_for_absence = reason_for_absence
            time_in = ""
            time_out = ""
        
        # Logic for half day absent codes
        elif reason_for_absence in ["AM leave", "PM leave"]:
            hours_worked = 3
            reason_for_absence = reason_for_absence
            if reason_for_absence == "AM leave":
                time_in = "02:00pm"
                time_out = "05:00pm"
            else:
                time_in = "09:00am"
                time_out = "12:00pm"
                
        else:
            hours_worked = 8
            reason_for_absence = ""
            time_in = "09:00am"
            time_out = "09:00am"


        # Fill in rows on specified columns with data(value)
        ws.cell(row=row_num, column=1, value=date_obj.strftime("%Y-%m-%d"))
        ws.cell(row=row_num, column=2, value=weekday)
        ws.cell(row=row_num, column=3, value=reason_for_absence)
        ws.cell(row=row_num, column=4, value=time_in)
        ws.cell(row=row_num, column=5, value=time_out)
        ws.cell(row=row_num, column=6, value=hours_worked)

        for col in range(1, 7):
            ws.cell(row=row_num, column=col).alignment = center_align
            ws.cell(row=row_num, column=col).border = thin_border

    for col in range(1, 7):
        col_letter = get_column_letter(col)
        ws.column_dimensions[col_letter].width = 15

    out_file = os.path.join(TMP_DIR, f"timesheet_{uuid.uuid4()}.xlsx")
    wb.save(out_file)
    return out_file
