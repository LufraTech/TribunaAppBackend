from schemas.session import Session
from config import db
from sqlalchemy import create_engine,text

class SessionRepository:

    @staticmethod
    async def create_session(nome_sessao: str, idusuario: int, data_sessao: str, status_sessao: bool):
        async with db as session:
            async with session.begin():
                query = text(f'INSERT INTO camara(nome_sessao, idusuario,data_sessao,status_sessao) VALUES (:nome_sessao, :idusuario, :data_sessao, :status_sessao);')
                result = await session.execute(query, {""})

                await session.commit()


    @staticmethod
    async def get_users_session(id_sessao: int):
        async with db as session:
            async with session.begin():
                query = text(f" SELECT usuario.* FROM usuario JOIN usuario_sessao ON usuario.idusuario = usuario_sessao .idusuario WHERE usuario_sessao.idsessao = :id_sessao;")
                usuarios = await session.execute(query, {"id_sessao": id_sessao})
                usuarios = usuarios.fetchall()
                return usuarios
