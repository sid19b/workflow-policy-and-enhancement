from fastapi import FastAPI
from api.v1 import health,auth,workflows,users  
from core.config import APP_NAME

from dotenv import load_dotenv

load_dotenv()

app=FastAPI(title=APP_NAME)
app.include_router(health.router,prefix="/api/v1",tags=["Health"])  #it includes every routes from health.py
app.include_router(auth.router,prefix="/api/v1",tags=["auth"])
app.include_router(workflows.router,prefix="/api/v1",tags=["workflows"])
app.include_router(users.router,prefix="/api/v1",tags=["db_operations"])