from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date

class PacienteCreate(BaseModel):
    nome: str
    data_nacimento: date
    email: EmailStr
    telefone: str
    endereco: str
    cpf: str
    historico: Optional[List[str]] = []
    status: bool = True


class Paciente(PacienteCreate):
    id: int

    class Confg:
        orm_mode = True
