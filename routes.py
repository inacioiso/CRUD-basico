from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Usuario
from schemas import UserCreate, UserResponse, UserUpdate

router = APIRouter(prefix='/users', tags=["users"])


#Rota POST
@router.post("/", response_model=UserResponse)
def cresateUser(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(Usuario).filter(Usuario.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="email alyread exist")
    else:
        new_user = Usuario(
            name = user.name,
            email = user.email,
            password = user.password
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

#Rota GET
@router.get("/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    users = db.query(Usuario).all()
    if users:
        return users
    else:
        raise HTTPException(status_code=404, detail="Not User alyread exist")

#Rota PUT
@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id:int, user_data:UserUpdate, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not user :
        raise HTTPException(status_code=404, detail="User not found")
    if user_data.name is not None:
        user.name = user_data.name
    if user_data.password is not None:
        user.password = user_data.password

    db.commit()
    db.refresh(user)
    return user

#Rota DELETE
@router.delete("/{user_id}", response_model=UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):  
    user = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not user :
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
