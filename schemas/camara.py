from pydantic import BaseModel


class Camara(BaseModel):
    idcamara: int | None = None
    nome_camara: str
    idcidade: int
    foto_camara: str | None = None
    cep: str