from typing import List, Optional
from models.dentista import Dentista

dentista_db: List[Dentista] = []

def criar_dentista(dentista: Dentista) -> Dentista:
    dentista_db.append(dentista)
    return dentista

def listar_dentista() -> List[Dentista]:
    return dentista_db

def buscar_dentista_id(id: int) -> Optional[Dentista]:
    return next((d for d in dentista_db if d.id == id), None)

def atualizar_dentista(id: int, dentista_atualizado: Dentista) -> bool:
    dentista = buscar_dentista_id(id)
    if dentista:
        dentista.nome = dentista_atualizado.nome
        dentista.especialidade = dentista_atualizado.especialidade
        dentista.cro = dentista_atualizado.cro
        return True
    return False

def deletar_dentista(id: int) -> bool:
    dentista = buscar_dentista_id(id)
    if dentista:
        dentista_db.remove(dentista)
        return True
    return False
