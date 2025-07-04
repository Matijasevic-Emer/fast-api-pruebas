from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import date

class Veterinarian(BaseModel):
    id: int
    first_name: str
    last_name: str
    license_number: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    obs: Optional[str]
    rate: Optional[str]
    tags: Optional[str]
    clinic_id: str

class Clinic(BaseModel):
    id: int
    name: str
    addres: str
    map: Optional[str]
    especiality: Optional[str]
    tags: Optional[str]

class Pet(BaseModel):
    id: int
    name: str = Field(default='Ruffian',min_length=3, max_length=40)
    species: str = Field(default='Gato/Perro/Tortuga',min_length=3)
    breed: str = Field(default='Mestizo/Doberman/ShortTail/etc',min_length=3)
    sex: str
    birth_date: date
    owner_name: str
    owner_phone: str
    sex: Optional[Literal["Male", "Female"]] = None  # Opcional, con valor por defecto None

    def to_dict(self):
        return {
           "id": self.id,
           "name": self.name 
        }

class MedicalVisit(BaseModel):
    id: int
    date: date
    reason: str
    notes: Optional[str]
    price: Optional[str]
    pet_id: int
    veterinarian_id: int
    weight_history_id: Optional[int]
   

class MedicalStudy(BaseModel):
    id: int
    type: str
    date: date
    results: Optional[str]
    pet_id: int
    medical_visit_id: Optional[int]

class File(BaseModel):
    id: int
    file_name: str
    file_type: str
    file_blob: Optional[str]
    url: str
    related_entity_type: str
    related_entity_id: int

class Diet(BaseModel):
    id: int
    start_date: date
    end_date: date
    observations: Optional[str]
    acceptance_level: str
    contraindications: Optional[str]
    formulated_by: str
    pet_id: int

class DietIngredient(BaseModel):
    id: int
    ingredient_name: str
    quantity: str
    diet_id: int

class Event(BaseModel):
    id: int
    description: str
    start_date: date
    end_date: date
    notes: Optional[str]
    pet_id: int

class Allergy(BaseModel):
    id: int
    type: str
    description: Optional[str]
    pet_id: int

class WeightHistory(BaseModel):
    id: int
    date: date
    weight: float
    pet_id: int

class Treatment(BaseModel):
    id: int
    type: str
    description: Optional[str]
    start_date: date
    end_date: date
    pet_id: int

class Surgery(BaseModel):
    id: int
    type: str
    date: date
    notes: Optional[str]
    pet_id: int

class Birth(BaseModel):
    id: int
    date: date
    number_of_puppies: int
    notes: Optional[str]
    pet_id: int
