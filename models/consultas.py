from pydantic import BaseModel
from datetime import datetime

class Consulta(BaseModel):
    id: int
    paciente_id: int
    dentista_id: int
    data_hora: datetime
    status: str #exempo: agendada, realizada, cancelada
    observacoes: str = ""