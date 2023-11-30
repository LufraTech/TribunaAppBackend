from schemas.camara import Camara
from config import db
from sqlalchemy import text

class CamaraRepository:

    # @staticmethod
    # async def create(camara_data: Camara):
    #     conn = await db.engine.begin()
    #     query = f'INSERT INTO camara(cidade_camara, cep) VALUES (camara_data.cidade_camara, camara_data.cep)'
    #     await conn.execute(text(query))
    #     await conn.commit()
    #     await conn.close()

    @staticmethod
    async def create_camara(camara_data: Camara):
        nome_camara = camara_data.nome_camara
        idcidade = camara_data.idcidade
        cep = camara_data.cep
        foto_camara = camara_data.foto_camara
        async with db as session:
            async with session.begin():
                query = text(f'INSERT INTO camara(nome_camara, idcidade,foto_camara, cep) VALUES (:nome_camara, :idcidade, :foto_camara, :cep);')
                await session.execute(query, {'nome_camara': nome_camara, 'idcidade': idcidade, 'foto_camara': foto_camara, 'cep': cep})
                await session.commit()
    @staticmethod
    async def update_camara( nome_camara: str, idcamara: int):
        async with db as session:
            async with session.begin():
                query = text(f"UPDATE camara SET nome_camara = :nome_camara WHERE camara.idcamara = {str(idcamara)};")
                await session.execute(query, {'nome_camara': nome_camara})
                await session.commit()

    # @staticmethod
    # async def delete_camara(idcamara:int):
    #     async with db as session:
    #             query = sqldelete(Camara).where(Camara.idcamara == idcamara)
    #             await session.execute(query)
    #             await db.commit_rollback()

    @staticmethod
    async def delete_camara(idcamara: int):
        async with db as session:
            async with session.begin():
                query = text(f"DELETE FROM camara WHERE camara.idcamara = {str(idcamara)};")
                await session.execute(query)
                await session.commit()

    # @staticmethod
    # async def create(usuario_):
    #
    # @staticmethod
    # async def delete(id: int):
    #     conn = await db.engine.begin()
    #     query =
    #     await conn.execute(text(query))
    #     await conn.commit()
    #     await conn.close()
    #
    # @staticmethod
    # async def get_all():
    #     conn = await db.engine.begin()
    #     query = "SELECT * FROM pessoa"
    #     pessoa = await conn.execute(text(query))
    #     pessoa = pessoa.fetchall()
    #     await conn.close()
    #     return pessoa
    #
    #
    #
    # @staticmethod
    # async def get_by_id(id: int = None):
    #     conn = await db.engine.begin()
    #     query =f"SELECT * FROM pessoa WHERE pessoa.id = {id}"
    #     pessoa = await conn.execute(text(query))
    #     pessoa = pessoa.fetchone()
    #     await conn.close()
    #     return pessoa
    #
    # @staticmethod
    # async def update(id: int, pessoa_data: Pessoa):
    #     conn = await db.engine.begin()
    #     query = f"UPDATE pessoa SET nome = '{pessoa_data.nome}', idade = {pessoa_data.idade} WHERE pessoa.id = {id}"
    #     await conn.execute(text(query))
    #     await conn.commit()
    #     await conn.close()
