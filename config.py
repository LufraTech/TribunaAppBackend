import os
from dotenv import load_dotenv
from sqlalchemy import create_engine,text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlmodel import SQLModel


load_dotenv()

DB_CONFIG = os.getenv("DB_CONFIG")


class DatabaseSession:
    def __init__(self, url: str = DB_CONFIG):
        self.engine = create_async_engine(url,echo=True)
        self.sessionLocal = sessionmaker(
            bind = self.engine,
            class_= AsyncSession,
            expire_on_commit=False
        )

    async def create_all(self):
        async with self.engine.begin() as conn:
           await conn.run_sync(SQLModel.metadata.create_all)

    async def drop_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.drop_all)

    async def close(self):
        await self.engine.dispose()

    async def __aenter__(self) -> AsyncSession:
        self.session = self.sessionLocal()
        return self.session

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

    async def get_db(self)->AsyncSession:
        async with self as db:
            yield db

    async def commit_rollback(self):
        try:
            await self.session.commit()
        except Exception as e:
            await self.session.rollback()
            raise e


db = DatabaseSession()
#
# if not DB_CONFIG:
#     print("DB_CONFIG is not set. Please check your .env file.")
#     exit(1)
#
# async def test_db_connection():
#     try:
#         # Create an asynchronous SQLAlchemy engine using the DB_CONFIG
#
#         # Use an asynchronous context manager to connect
#         async with db.engine.begin() as conn:
#             # Execute a simple query to test the connection
#             query = "SELECT * FROM usuario"
#
#             result = await conn.execute(text(query))
#             print(result)
#             value = result.fetchall()
#             print(value)
#
#         # Check if the query was successful
#         # if value == 1:
#         #     print("Connected to the database successfully.")
#         # else:
#         #     print("Failed to connect to the database.")
#     except Exception as e:
#         print(f"Error: {e}")
# #
# # Run the asynchronous function
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(test_db_connection())