from schemas.politicalparty import PoliticalParty
from config import db
from sqlalchemy import create_engine,text

class PoliticalPartyRepository:

    @staticmethod
    async def create_political_party(polical_party: PoliticalParty):
        nome_partido = polical_party.nome_partido
        sigla_partido = polical_party.sigla_partido
        deferimento = polical_party.deferimento
        presidente_nacional = polical_party.presidente_nacional
        numero_legenda = polical_party.numero_legenda
        async with db as session:
            async with session.begin():
                query = text(f'INSERT INTO partido(nome_partido, sigla_partido, deferimento, presidente_nacional, numero_legenda) VALUES (:nome_partido, :sigla_partido, :deferimento, :presidente_nacional, :numero_legenda);')
                await session.execute(query, {"nome_partido": nome_partido,
                                              "sigla_partido": sigla_partido,
                                              "deferimento": deferimento,
                                              "presidente_nacional": presidente_nacional,
                                              "numero_legenda": numero_legenda})
                await session.commit()