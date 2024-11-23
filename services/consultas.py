from typing import List, Optional
from models.consultas import Consulta

consultas_db: List[Consulta] = []


def criar_consulta(consulta: Consulta) -> Consulta:
    consultas_db.append(consulta)
    return consulta

def listar_consulta() -> List[Consulta]:
    return consultas_db

def buscar_consulta_id(id: int) -> Optional[Consulta]:
    return next((c for c in consultas_db if c.id == id), None)

def deletar_consulta(id: int) -> bool:
    consulta = buscar_consulta_id(id)
    if consulta:
        consultas_db.remove(consulta)
        return True
    return False

def atualizar_consulta(id: int, consulta_atualizada: Consulta) -> bool:
    consulta = buscar_consulta_id(id)
    if consulta:
        consulta.observacoes = consulta_atualizada.observacoes
        consulta.data_hora = consulta_atualizada.data_hora
        consulta.dentista_id = consulta_atualizada.dentista_id
        consulta.paciente_id = consulta_atualizada.paciente_id
        return True
    return False