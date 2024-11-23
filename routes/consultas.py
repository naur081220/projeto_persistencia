from fastapi import APIRouter, HTTPException
from typing import List
from models.consultas import Consulta
from services.consultas import criar_consulta, listar_consulta , buscar_consulta_id, atualizar_consulta, deletar_consulta

router = APIRouter()

@router.post("/consultas/", response_model=Consulta)
def criar_consulta_nova(consulta: Consulta):
    return criar_consulta(consulta)

@router.get("/consulta/", response_model=List[Consulta])
def listar():
    return listar_consulta()


@router.get("/consulta/{id}", response_model=Consulta)
def buscar_consulta(id: int):
    consulta = buscar_consulta_id(id)
    if not consulta:
        raise HTTPException(status_code=404, detail="Consulta não encontrada")
    return consulta

@router.put("/consulta/{id}", response_model=Consulta)
def atualizar_consulta_existente(id: int, consulta_atualizada: Consulta):
    consulta = buscar_consulta_id(id)
    if not consulta:
        raise HTTPException(status_code=404, detail="Consulta não encontrada")
    if not atualizar_consulta(id, consulta_atualizada):
        raise HTTPException(status_code=400, detail="Falha ao atualizar consulta")
    return consulta_atualizada

@router.delete("/consulta/{id}", response_model=dict)
def deletar_consulta_existente(id: int):
    if not deletar_consulta(id):
        raise HTTPException(status_code=404, detail="Consulta não encontrada")
    return {"detail": "Consulta deletada com sucesso"}