from pydantic import BaseModel
from datetime import datetime

class Session(BaseModel):

    idsessao: int
    nome_sessao: str
    idusuario: int
    data_sessao: datetime
    status_sessao: bool