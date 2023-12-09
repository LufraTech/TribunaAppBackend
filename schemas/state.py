from pydantic import BaseModel


class State(BaseModel):

    idestado: int | None = None
    nome_estado: str
