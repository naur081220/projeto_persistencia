from fastapi import APIRouter, HTTPException
from typing import List
from models.paciente import PacienteCreate, Paciente
from services.paciente import (
    criar_paciente,
    listar_pacientes,
    buscar_paciente_id,
    atualizar_paciente,
    deletar_paciente,
)

router = APIRouter()

@router.post("/pacientes/", response_model=Paciente)
async def criar_paciente_endpoint(paciente: PacienteCreate):
    try:
        return await criar_paciente(paciente)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/pacientes/", response_model=List[Paciente])
async def listar_pacientes_endpoint():
    return await listar_pacientes()

@router.get("/pacientes/{id}", response_model=Paciente)
async def buscar_paciente_endpoint(id: int):
    paciente = await buscar_paciente_id(id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return paciente

@router.put("/pacientes/{id}", response_model=Paciente)
async def atualizar_paciente_endpoint(id: int, paciente_atualizado: PacienteCreate):
    paciente = await buscar_paciente_id(id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    paciente_atualizado = await atualizar_paciente(id, paciente_atualizado)
    if not paciente_atualizado:
        raise HTTPException(status_code=400, detail="Falha ao atualizar paciente")
    return paciente_atualizado

@router.delete("/pacientes/{id}", response_model=dict)
async def deletar_paciente_endpoint(id: int):
    if not await deletar_paciente(id):
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return {"detail": "Paciente deletado com sucesso"}
