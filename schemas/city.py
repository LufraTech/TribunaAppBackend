from pydantic import BaseModel


class City(BaseModel):
    idcidade: int | None = None
    nome_cidade: str
    idestado: int | None = None


class CityUpdate(BaseModel):
    idcidade: int
    nome_cidade: str | None = None
    idestado: int | None = None