from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routes import clinic, pet
from homeview import homeview

app = FastAPI(
    title="Historia Canina Management API",
    description="API para administrar Historia Clinica Canina.",
    version="1.0.0"
)

# Registrar rutas
app.include_router(clinic.router, prefix="/api")
app.include_router(pet.router, prefix="/api")

# @app.get("/")
# async def root():
#     return {"message": "Welcome to the Veterinary Management API"}

# decorador para establecer la ruta y luego una funcion que lee el root
@app.get('/', tags=['inicio'])
def read_root():
    html_content = homeview()
    return HTMLResponse(content=html_content)
