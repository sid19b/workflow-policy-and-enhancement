import os
import json 
from dotenv import load_dotenv

load_dotenv()


APP_NAME=os.getenv("APP_NAME","SECURE_FLOW")
ENV=os.getenv("ENV","DEV")
DEBUG_MODE=os.getenv("DEBUG_MODE",True)

############################### DB_CONFIG ###############################

DB_HOST=os.getenv("DB_HOST","localhost")
DB_PORT=os.getenv("DB_PORT","3306")
DB_NAME=os.getenv("DB_NAME","secure_workflow_db")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")