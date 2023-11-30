from pydantic import BaseModel


class PoliticalParty(BaseModel):

    nome_partido: str
    sigla_partido: str
    deferimento: str
    presidente_nacional: str
    numero_legenda: int