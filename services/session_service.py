from schemas.session import Session
from config import db
from sqlalchemy import create_engine,text
from schemas.session import Session

class SessionRepository:

    @staticmethod
    async def create_session(session: Session):
        nome_sessao = session.nome_sessao
        data_agendamento_sessao = session.data_agendamento_sessao
        data_sessao = session.data_sessao
        status_sessao = session.status_sessao
        async with db as session:
            async with session.begin():
                query = text(f'INSERT INTO camara(nome_sessao, data_agendamento_sessao,data_sessao,status_sessao) VALUES (:nome_sessao, :data_agendamento_sessao, :data_sessao, :status_sessao);')
                await session.execute(query, {"nome_sessao": nome_sessao,
                                              "data_agendamento_sessao": data_agendamento_sessao,
                                              "data_sessao": data_sessao,
                                              "status_sessao": status_sessao})
                await session.commit()

    @staticmethod
    async def get_users_session(id_sessao: int):
        async with db as session:
            async with session.begin():
                query = text(f" SELECT usuario.* FROM usuario JOIN usuario_sessao ON usuario.idusuario = usuario_sessao .idusuario WHERE usuario_sessao.idsessao = :id_sessao;")
                usuarios = await session.execute(query, {"id_sessao": id_sessao})
                usuarios = usuarios.fetchall()
                return usuarios
