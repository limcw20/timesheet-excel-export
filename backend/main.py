from fastapi import FastAPI
from routes.timesheet import router as timesheet_router

app = FastAPI()

app.include_router(timesheet_router, prefix="/timesheet")