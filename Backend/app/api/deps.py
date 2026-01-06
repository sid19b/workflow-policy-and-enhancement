from fastapi import Depends
from sqlalchemy.orm import Session 
from db.session import SessionLocal

def get_db():
    try:
        db=SessionLocal() #The FastAPI Framework calls next() at the start and end of every web request.
        yield db
    finally:
        db.close()
