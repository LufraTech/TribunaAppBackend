from pydantic import BaseModel


class Camara(BaseModel):

    nome_camara: str
    idcidade: int
    foto_camara: str | None = None
    cep: str