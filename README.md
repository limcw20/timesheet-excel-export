*Last edited 10 Dec 2025
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

### Tech Stack (Tentative till Project Dev Start):
- Frontend: Vue 3 Composition API or React 19
- Frontend Tools: Pinia, Vuetify
- Backend: FastAPI
- Backend Libraries: OpenPYXL
- Local Deployment: NPM (Vue/React) , Uvicorn (FastAPI)
- Other Deployments: Docker (possibly sharing)

 *Online deployment not needed
