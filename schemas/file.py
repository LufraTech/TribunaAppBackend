from pydantic import BaseModel


class File(BaseModel):

    nome_arquivo: str
    idsessao: int