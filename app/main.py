from fastapi import FastAPI
from app.api import itemController

app = FastAPI()

#Implementar Rutas o Controllers
app.include_router(itemController.router, prefix="/api/v1")

#Endpoint que devuelve un mensaje
@app.get("/")
def message():
    return "Hello world"