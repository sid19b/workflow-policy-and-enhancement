from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from schemas.user import UserCreate,UserRead
from models.user import user
from api.deps import get_db

router=APIRouter()

@router.post("/users",response_model=UserRead)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    # 1. Convert Schema data to Database Model
    new_user = user(
        username=user_in.username,
        email=user_in.email
    )
    
    # 2. Add to the "staging area"
    db.add(new_user)
    
    # 3. Save to the database
    db.commit()
    
    # 4. Refresh to get the ID from the database
    db.refresh(new_user)
    
    # 5. Return the result (FastAPI converts this to UserRead automatically)
    return new_user