from fastapi import APIRouter,Query 
from fastapi.responses import JSONResponse
from typing import List
from models import Pet

router = APIRouter()

# Simulación de base de datos
pets_db = []

@router.get("/pets", response_model=List[Pet], tags=["Pets"])
async def get_pets():
    return pets_db

@router.get("/pets/{pet_id}", response_model=Pet, tags=["Pets"])
async def get_pet(pet_id: int):
    pet = next((p for p in pets_db if p.id == pet_id), None)
    if not pet:
        return {"error": "Pet not found"}
    return pet

@router.post("/pets", response_model=Pet, tags=["Pets"])
async def create_pet(pet: Pet):
    pets_db.append(pet)
    return JSONResponse(content={'messagge':'Creado exitosamente','pet':pet.to_dict()})

@router.put("/pets/{pet_id}", response_model=Pet, tags=["Pets"])
async def update_pet(pet_id: int, updated_pet: Pet):
    for idx, pet in enumerate(pets_db):
        if pet.id == pet_id:
            pets_db[idx] = updated_pet
            return updated_pet
    return {"error": "Pet not found"}

@router.delete("/pets/{pet_id}", tags=["Pets"])
async def delete_pet(pet_id: int):
    global pets_db
    pets_db = [p for p in pets_db if p.id != pet_id]
    return {"message": f"Pet with id {pet_id} deleted"}
