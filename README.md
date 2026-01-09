### LATEST UPDATE (09/01/26)
- Added bottom part of the template (also the final):
  - Staff name + date of timesheet preparation
  - Supervisor name + date + signature, to be filled by supervisor
- Initialize .env and used for the following:
  - File directory
  - File name
  - Staff name
  - Staff reference number
- Removed obsolete code
- Added "Guide" section in README, contains example .env and json payload for now
</br>

# Export for Timesheet

<strong>ISSUE:</strong>
</br>
I spend a lot of time manually editing my Excel timesheet at work every month (e.g. edit details such as dates, days, row highlights, etc.)
</br>
Below is a sample of the timesheet template given to me to submit every month. All annotations represent what I usually have to edit every month.
<img width="1083" height="762" alt="image" src="https://github.com/user-attachments/assets/6ed8188c-99db-49c8-a281-8463ca1f0426" />
</br>

## Technical Diagram
<img width="1187" height="790" alt="image" src="https://github.com/user-attachments/assets/6c59452e-460e-49b5-99d2-64387d750aa8" />

No database needed. I had a realization that just writing the JSON payload on Postman is sufficient, hence I will shelf the idea for frontend.
</br>

## Tech Stack:

- Backend: FastAPI
- Backend Libraries: OpenPYXL
- Local Deployment:  Uvicorn (FastAPI)
- Other Deployments: Docker (possibly for sharing)

\*Online deployment not needed


# Guide

### Example .env values
These are the variables and example values that used:
````
FILE_DIRECTORY=Documents/timesheets
TIMESHEET_FILENAME=2601_timesheet
STAFF_NAME=John Doe
STAFF_REF_NO=EMP9998
````

### Example JSON payload
**Method:** POST
</br>
**HTTP URL:** http://{your_local_server_here}/timesheet/export
</br>
**Raw JSON payload in request body:**
````
{
  "start_year": 2026,
  "start_month": 1,
  "entries": [
    {"day_of_month": 3,"reason_for_absence": "AL"},
    {"day_of_month": 12,"reason_for_absence": "AM leave"},
    {"day_of_month": 16,"reason_for_absence": "PM leave"},
    {"day_of_month": 20,"reason_for_absence": "half day"},
    {"day_of_month": 21,"reason_for_absence": "PH"},
    {"day_of_month": 6,"ot_from":"06:00pm","ot_to":"08:00pm","ot_hours":2,"ot_approved_by":"Jane Doe"}
  ]
}
````

## Changelog:

### 08/01/26
- Modified README:
  - Technical Diagram changes (renamed from Planning Stage)
  - Changelog from recent to oldest (top-down)
  - remove obsolete texts
- Added Columns and autofill logic for overtime work
- Refactor code: StreamingResponse to FileResponse, some values
- Excel template adjustments
- Fix codes with incorrect variables

### 07/01/26
- Added comments to codes for easier code editing and referencing (I will do it as I code along from today onwards, whoops)
- Further developed the timesheet template:
  - Title, Employee reference number, date range, employee name
  - Adjusted column widths
  - Added Time in & Time out columns
  - Reordered table headers, swapping "Date" and "Day", and "Remarks" changed to "Reason for Absence"
  - Background colour highlighting on specific dates (Weekends, Holidays, Leaves)
- Autofill time in & time out data unless specified in payload, logic to handle different absent codes such as:
  - "PH", "MC", "UPL","AL" on Reason for Absence -> blank for time in & time out
  - "PM leave", "half day" on Reason for Absence -> autofill time in: 9am, timeout:12pm, hours worked: 3
  - "AM leave" on Reason for Absence -> autofill time in: 2pm, timeout: 5pm, hours worked: 3
 
### 02/01/26
- Adjusted to correct date loop (4th of specified month to 3rd of following month)
- Logic to exclude autofill data on weekends, and allow dates to be overwritten if specified on payload
- Improved payload for date entry -> integer format representing day of month (e.g. 1, 2, 3,..31) instead of date format
- Minor Code reordering for export excel API call

### 31/12/25
Went missing due to military service and eye surgery :-P
- Started on base structure of Excel Template.
- Setup for excel generation API call, payload in JSON format.
- Dates in excel are auto-filled according to month and year provided. (Starts at 3rd day of month for now)
- Excel temporarily exports to project folder for ease of testing, will be shifted to .env after structure is finalized.

### 10/12/25
- Init project + README
- Background Issue & Planning




