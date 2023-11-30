from schemas.file import File
from sqlalchemy import text
from config import db

class FileRepository:

    @staticmethod
    async def create_file(file_data: File):
        nome_arquivo = file_data.nome_arquivo
        idsessao = file_data.idsessao
        async with db as session:
            async with session.begin():
                query = text(f'INSERT INTO arquivo(nome_arquivo, idsessao) VALUES (:nome_arquivo, :idsessao)')
                await session.execute(query, {"nome_arquivo": nome_arquivo, "idsessao": idsessao})
                await session.commit()

