from pydantic import BaseModel
from datetime import datetime

class Session(BaseModel):

    idsessao: int | None = None
    nome_sessao: str
    data_agendamento_sessao: datetime
    data_sessao: datetime
    status_sessao: str
    hora_termino_sessao: datetime | None = None

