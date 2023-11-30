from datetime import timedelta,datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from sqlalchemy import text
from config import db
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer


class Token(BaseModel):
    access_token: str

SECRET_KEY = "09d25e094faz6ca2556c8157478b7a3b93adsdf7099f6f0f4caa6cf63y5643e9"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



async def authenticate_user(email_usuario: str, senha_usuario: str):
    async with db as session:
        async with session.begin():
            query = text( "SELECT * FROM usuario WHERE email_usuario = :email_usuario")
            user = await session.execute(query, {"email_usuario": email_usuario})
            user = user.fetchone()
    print(user)
    if not user:
        return False
    if not bcrypt_context.verify(senha_usuario, user.senha_usuario):
        return False
    return user


def create_access_token(email_usuario: str, id: int, expires_delta: timedelta):
    encode = {"sub": email_usuario, "id": id}
    expire = datetime.utcnow() + expires_delta
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)



