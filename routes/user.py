from fastapi import APIRouter,Query 
from fastapi.responses import JSONResponse
from typing import List
from models import User
from user_jwt import createToken

router = APIRouter()

# Simulación de base de datos
user_db = []

@router.get("/users", response_model=List[User], tags=["Users"])
async def get_users():
    return users_db

@router.post("/login", tags=["Authentication"])
async def create_user(user: User):
    return createToken(user.to_dict())

@router.put("/users/{user_id}", response_model=User, tags=["Users"])
async def update_user(user_id: int, updated_user: User):
    for idx, user in enumerate(users_db):
        if user.id == user_id:
            users_db[idx] = updated_user
            return updated_user
    return {"error": "User not found"}

@router.delete("/users/{user_id}", tags=["Users"])
async def delete_user(user_id: int):
    global users_db
    users_db = [p for p in users_db if p.id != user_id]
    return {"message": f"User with id {user_id} deleted"}
