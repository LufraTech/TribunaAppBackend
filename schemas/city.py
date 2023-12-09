from pydantic import BaseModel


class City(BaseModel):

    nome_cidade: str
    idestado: int | None = None


class CityUpdate(BaseModel):
    idcidade: int
    nome_cidade: str | None = None
    idestado: int | None = None