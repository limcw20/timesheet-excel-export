
*Currently recovering from eye surgery.
</br>

### LATEST UPDATE (07/01/26)
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
</br>

# Export for Timesheet

<strong>ISSUE:</strong>
</br>
I spend a lot of time manually editing my Excel timesheet at work every month (e.g. edit details such as dates, days, row highlights, etc.)
</br>
Below is a sample of the timesheet template given to me to submit every month. All annotations represent what I usually have to edit every month.
<img width="1083" height="762" alt="image" src="https://github.com/user-attachments/assets/6ed8188c-99db-49c8-a281-8463ca1f0426" />
</br>

## Planning Stage

<img width="960" height="671" alt="image" src="https://github.com/user-attachments/assets/dc31709c-e0f4-4752-8c70-c33ea22a7284" />
Currently, I do not foresee a need for a database, as there is no reason to retain the timesheets after submission.
</br>

### Some things to consider:
- Default Values such as Contract Reference No., Name of Staff, Signature. Values can be in .env file
- Dynamic Values such as Dates, Days, Period. Can be based on current date.
- Auto Row Highlights depending on situations (weekends, MC, AL)

### Tech Stack:

- Frontend: Vue 3 Composition API
- Frontend Tools: Pinia, Vuetify
- Backend: FastAPI
- Backend Libraries: OpenPYXL
- Local Deployment: NPM (Vue) , Uvicorn (FastAPI)
- Other Deployments: Docker (possibly for sharing)

  \*Online deployment not needed



## Changelog:

### 10/12/25
- Init project + README
- Background Issue & Planning

### 31/12/25
Went missing due to military service and eye surgery :-P
- Started on base structure of Excel Template.
- Setup for excel generation API call, payload in JSON format.
- Dates in excel are auto-filled according to month and year provided. (Starts at 3rd day of month for now)
- Excel temporarily exports to project folder for ease of testing, will be shifted to .env after structure is finalized.

### 02/01/26
- Adjusted to correct date loop (4th of specified month to 3rd of following month)
- Logic to exclude propagated data on weekends, and allow dates to be overwritten if specified on payload
- Improved payload for date entry -> integer format representing day of month (e.g. 1, 2, 3,..31) instead of date format
- Minor Code reordering for export excel API call
