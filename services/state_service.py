from sqlalchemy import text
from config import db
from schemas.state import State

class StateRepository:

    @staticmethod
    async def create_state(state_data:State):
        nome_estado = state_data.nome_estado

        async with db as session:
            async with session.begin():

                query = text(f'INSERT INTO estado(nome_estado) VALUES (:nome_estado);')
                await session.execute(query, {"nome_estado": nome_estado})
                await session.commit()

    @staticmethod
    async def get_all_state():
        async with db as session:
            async with session.begin():
                query = text(f'SELECT * FROM estado')
                result = await session.execute(query)
                result = result.fetchall()
                return result