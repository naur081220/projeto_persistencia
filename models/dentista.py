from pydantic import BaseModel, EmailStr
from typing import List
from datetime import date

class Dentista(BaseModel):
    id: int
    nome: str
    cro: str # Conselho Regional de Odontologia
    especialidade: str
    telefone: str
    email: EmailStr
    status: bool = True