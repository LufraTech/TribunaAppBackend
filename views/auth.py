from datetime import timedelta,datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from config import db
from passlib.context import  CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy import text
from collections import Counter
from schemas.user import User
import asyncio


router_auth = APIRouter(
    prefix='/auth',
    tags=['Auth']
)
class Token(BaseModel):
    access_token: str

SECRET_KEY = "09d25e094faz6ca2556c8157478b7a3b93adsdf7099f6f0f4caa6cf63y5643e9"
ALGORITHM = "HS256"


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

class CreateUserRequest(BaseModel):
    email_usuario: str
    senha_usuario: str

class Token(BaseModel):
    access_token: str
    token_type: str

db_dependency = Annotated[Session, Depends(db.get_db)]


@router_auth.post('/',status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, user_data: CreateUserRequest):

    create_user_model = User(
        email_usuario=user_data.email_usuario,
        senha_usuario=bcrypt_context.hash(user_data.senha_usuario)
    )
    db.add(create_user_model)
    db.commit()

@router_auth.post('/token',response_model=Token)
async def login_for_access_token(form_data: Annotated[CreateUserRequest, Depends()]):
    user = await authenticate_user(form_data.email_usuario, form_data.senha_usuario)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
    token = create_access_token(form_data.email_usuario, user.idusuario ,timedelta(minutes=15))
    result = {"access_token": token, "token_type": "bearer"}
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
async def authenticate_user(email_usuario: str, senha_usuario: str):
    async with db as session:
        async with session.begin():
            query = text("SELECT * FROM usuario WHERE email_usuario = :email_usuario")
            user = await session.execute(query, {"email_usuario": email_usuario})
            user = user.fetchone()

            print(user)
            if not user:
                return False
            if not bcrypt_context.verify(senha_usuario, user.senha_usuario):
                return False
            return user


def create_access_token(email_usuario: str, id: int, expires_delta: timedelta = None):
    encode = {"sub": email_usuario, "id": id}
    expire = datetime.utcnow() + expires_delta
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        id = payload.get("id")
        if email is None or id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

        msg ={"email": email, "id": id}
        return JSONResponse(status_code=status.HTTP_200_OK, content=msg)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

# def create_access_token(email_usuario: str, id: int, expires_delta: timedelta = None):
#     encode = {"sub": email_usuario, "id": id}
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     encode.update({"exp": expire})
#     return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)