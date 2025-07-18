from schemas.user import User
from config import db
from sqlalchemy import create_engine, text
from datetime import datetime
from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserRepository:

    @staticmethod
    async def create_user(user_data: User):
        primeiro_nome = user_data.primeiro_nome
        sobrenome = user_data.sobrenome
        senha_usuario = user_data.senha_usuario = bcrypt_context.hash(user_data.senha_usuario)
        email_usuario = user_data.email_usuario
        foto_perfil = user_data.foto_perfil
        idpartido = user_data.idpartido
        usuario_presidente = user_data.usuario_presidente
        usuario_vereador = user_data.usuario_vereador
        usuario_administrador = user_data.usuario_administrador
        idcamara = user_data.idcamara
        status = user_data.status

        async with db as session:
            async with session.begin():
                query = text(
                    f'INSERT INTO usuario(primeiro_nome,sobrenome, senha_usuario, email_usuario,foto_perfil, idpartido, usuario_vereador, usuario_presidente, usuario_administrador, idcamara,status) VALUES (:primeiro_nome, :sobrenome, :senha_usuario, :email_usuario,:foto_perfil, :idpartido, :usuario_presidente, :usuario_vereador, :usuario_administrador, :idcamara, :status);')
                await session.execute(query, {"primeiro_nome": primeiro_nome,
                                              "sobrenome": sobrenome,
                                              "senha_usuario": senha_usuario,
                                              "email_usuario": email_usuario,
                                              "foto_perfil": foto_perfil,
                                              "idpartido": idpartido,
                                              "usuario_presidente": usuario_presidente,
                                              "usuario_vereador": usuario_vereador,
                                              "usuario_administrador": usuario_administrador,
                                              "idcamara": idcamara,
                                              "status": status})
                await session.commit()

    @staticmethod
    async def delete_user(id: int):
        async with db as session:
            async with session.begin():
                query = text(f"DELETE FROM usuario WHERE usuario.idusuario = {str(id)};")
                await session.execute(query)
                await session.commit()
    #
    # @staticmethod
    # async def create_user(nome_usuario: str, password_usuario: str, idpartido: int, email_usuario: str,
    #                       usuario_administrador: bool, idcamara: int,
    #                       vereador: bool):
    #     async with db as session:
    #         async with session.begin():
    #             query = text(
    #                 f'INSERT INTO usuario(nome_usuario, password_usuario, idpartido, email_usuario, usuario_administrador, idcamara,vereador) VALUES (:nome_usuario, :password_usuario, :idpartido, :email_usuario, :usuario_administrador, :idcamara,:vereador);')
    #             await session.execute(query, {"nome_usuario": nome_usuario, "password_usuario": password_usuario,
    #                                           "idpartido": idpartido, "email_usuario": email_usuario,
    #                                           "usuario_administrador": usuario_administrador, "idcamara": idcamara,
    #                                           "vereador": vereador})
    #             await session.commit()

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
# @staticmethod
# async def get_by_id(id: int = None):
#     conn = await db.engine.begin()
#     query = f"SELECT * FROM pessoa WHERE pessoa.id = {id}"
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
