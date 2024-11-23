from fastapi import APIRouter, HTTPException
from typing import List
from models.dentista import Dentista
from services.dentista import criar_dentista, listar_dentista, buscar_dentista_id, atualizar_dentista, deletar_dentista

router = APIRouter()

@router.post("/dentista/", response_model=Dentista)
def criar(dentista: Dentista):
    return criar_dentista(dentista)

@router.get("/dentista/", response_model=List[Dentista])
def listar():
    return listar_dentista()

@router.get("/dentista/{id}", response_model=Dentista)
def buscar(id: int):
    dentista = buscar_dentista_id(id)
    if not dentista:
        raise HTTPException(status_code=404, detail="Dentista não encontrado")
    return dentista

@router.put("/dentista/{id}", response_model=Dentista)
def atualizar(id: int, dentista_atualizado: Dentista):
    dentista_existente = buscar_dentista_id(id)
    if not dentista_existente:
        raise HTTPException(status_code=404, detail="Dentista não encontrado")
    if not atualizar_dentista(id, dentista_atualizado):
        raise HTTPException(status_code=400, detail="Falha ao atualizar dentista")
    return dentista_atualizado

@router.delete("/dentista/{id}", response_model=dict)
def deletar(id: int):
    if not deletar_dentista(id):
        raise HTTPException(status_code=404, detail="Dentista não encontrado")
    return {"detail": "Dentista deletado com sucesso"}
