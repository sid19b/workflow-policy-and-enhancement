# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

#Module level

DB_URL=f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine=create_engine(DB_URL)

SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)