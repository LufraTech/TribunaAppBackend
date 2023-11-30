from sqlalchemy import text
from config import db
from schemas.city import CityUpdate,City

class CityRepository:

    @staticmethod
    async def create_city(city: City):
        nome_cidade = city.nome_cidade
        idestado = city.idestado
        async with db as session:
            async with session.begin():
                query = text(f'INSERT INTO cidade(nome_cidade,idestado) VALUES (:nome_cidade,:idestado)')
                await session.execute(query, {"nome_cidade": nome_cidade, "idestado": idestado})
                await session.commit()

    @staticmethod
    async def get_all_city():
        async with db as session:
            async with session.begin():
                query = text(f'SELECT * FROM cidade')
                result = await session.execute(query)
                result = result.fetchall()
                return result

    @staticmethod
    async def delete_city(idcidade: int):
        async with db as session:
            async with session.begin():
                query = text(f"DELETE FROM cidade WHERE cidade.idcidade = {str(idcidade)};")
                await session.execute(query)
                await session.commit()

    # @staticmethod
    # async def update_city(cidy_data: CityUpdate):
    #     nome_cidade = cidy_data.nome_cidade
    #     idestado = cidy_data.idestado
    #     async with db as session:
    #         async with session.begin():
    #             query = text(f"UPDATE cidade SET nome_cidade = :nome_cidade WHERE cidade.idestado = :idestado")
    #             await session.execute(query, {'nome_cidade': nome_cidade, "idestado": idestado})
    #             await session.commit()

    @staticmethod
    async def update_city(cidy_data: CityUpdate):
        nome_cidade = cidy_data.nome_cidade
        idcidade = cidy_data.idcidade
        async with db as session:
            async with session.begin():
                query = text(f"UPDATE cidade SET nome_cidade = :nome_cidade WHERE cidade.idcidade"
                             f" = :idcidade")
                await session.execute(query, {'nome_cidade': nome_cidade, "idcidade": idcidade})
                await session.commit()