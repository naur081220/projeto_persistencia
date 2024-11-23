from models.paciente import PacienteCreate, Paciente
from typing import List, Optional

fake_db: List[Paciente] = []

async def criar_paciente(paciente: PacienteCreate) -> Paciente:
    novo_paciente = Paciente(
        id=len(fake_db) + 1,
        nome=paciente.nome,
        data_nascimento=paciente.data_nascimento,
        telefone=paciente.telefone,
        email=paciente.email,
        endereco=paciente.endereco,
        cpf=paciente.cpf,
        historico=paciente.historico,
        status=paciente.status
    )
    fake_db.append(novo_paciente)
    return novo_paciente

async def listar_pacientes() -> List[Paciente]:
    return fake_db

async def buscar_paciente_id(id: int) -> Optional[Paciente]:
    return next((p for p in fake_db if p.id == id), None)

async def atualizar_paciente(id: int, paciente_atualizado: PacienteCreate) -> Optional[Paciente]:
    paciente = await buscar_paciente_id(id)
    if paciente:
        paciente.nome = paciente_atualizado.nome
        paciente.data_nascimento = paciente_atualizado.data_nascimento
        paciente.telefone = paciente_atualizado.telefone
        paciente.email = paciente_atualizado.email
        paciente.endereco = paciente_atualizado.endereco
        paciente.cpf = paciente_atualizado.cpf
        paciente.historico = paciente_atualizado.historico
        paciente.status = paciente_atualizado.status
        return paciente
    return None

async def deletar_paciente(id: int) -> bool:
    paciente = await buscar_paciente_id(id)
    if paciente:
        fake_db.remove(paciente)
        return True
    return False
