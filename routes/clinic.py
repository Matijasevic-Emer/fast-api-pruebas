from fastapi import APIRouter
from typing import List
from models import Clinic

router = APIRouter()

# Simulación de base de datos
clinics_db = []

@router.get("/clinics", response_model=List[Clinic], tags=["Clinics"])
async def get_clinics():
    return clinics_db

@router.get("/clinics/{clinic_id}", response_model=Clinic, tags=["Clinics"])
async def get_clinic(clinic_id: int):
    clinic = next((c for c in clinics_db if c.id == clinic_id), None)
    if not clinic:
        return {"error": "Clinic not found"}
    return clinic

@router.post("/clinics", response_model=Clinic, tags=["Clinics"])
async def create_clinic(clinic: Clinic):
    clinics_db.append(clinic)
    return clinic

@router.put("/clinics/{clinic_id}", response_model=Clinic, tags=["Clinics"])
async def update_clinic(clinic_id: int, updated_clinic: Clinic):
    for idx, clinic in enumerate(clinics_db):
        if clinic.id == clinic_id:
            clinics_db[idx] = updated_clinic
            return updated_clinic
    return {"error": "Clinic not found"}

@router.delete("/clinics/{clinic_id}", tags=["Clinics"])
async def delete_clinic(clinic_id: int):
    global clinics_db
    clinics_db = [c for c in clinics_db if c.id != clinic_id]
    return {"message": f"Clinic with id {clinic_id} deleted"}
