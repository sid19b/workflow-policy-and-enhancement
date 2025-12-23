from sqlalchemy import Column,Integer,String
from db.base import Base

#Base is required because it registers all ORM models with SQLAlchemy, allowing it to track table metadata and manage database mappings

class user(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)