from fastapi import FastAPI
from routes.paciente import router as paciente_router
from routes.dentista import router as dentista_router
from routes.consultas import router as consultas_router

app = FastAPI()

 # Inclui as rotas
app.include_router(paciente_router)
app.include_router(dentista_router)
app.include_router(consultas_router)