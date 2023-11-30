from fastapi import APIRouter, HTTPException, Response, status
from schemas.user import User
from services.user_service import UserRepository
from fastapi.responses import JSONResponse

from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

route_user = APIRouter(prefix='/user', tags=['User'])
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

@route_user.post('/create')
async def create_user(user_data: User):

    # email_db = await CreateUser.check_email(user_input.email)
    # if email_db != []:
    #     msg = {"message": f"Email: {user_input.email} já cadastrado"}
    #     return JSONResponse(content=msg, status_code=409)
    try:
        await UserRepository.create_user(user_data)

        msg = {
            "message": "Usuario criado com sucesso",
            "nome_usuario": user_data.nome_usuario,
            "email_usuario": user_data.email_usuario,
            "idpartido": user_data.idpartido,
            "idcamara": user_data.idcamara,
            "usuario_administrador": user_data.usuario_administrador,
            "usuario_presidente": user_data.usuario_presidente,
            "verador": user_data.vereador
            }
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=msg)

    except Exception as error:

        msg = {"message": error}
        print(msg)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))

@route_user.delete('/delete/{id}')
async def delete_user(id: int):
    try:
        await UserRepository.delete_user(id)
        msg = {"message": "Usuario deletado com sucesso"}
        return JSONResponse(status_code=status.HTTP_200_OK, content=msg)
    except Exception as error:
        msg = {"message": error}
        print(msg)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))

# @router_user.post('/create')
# async def create_user(user_data: User):
#
#     # email_db = await CreateUser.check_email(user_input.email)
#     # if email_db != []:
#     #     msg = {"message": f"Email: {user_input.email} já cadastrado"}
#     #     return JSONResponse(content=msg, status_code=409)
#
#     try:
#
#         await UserRepository.create_user(
#             user_data.nome_usuario,
#             user_data.senha_usuario,
#             user_data.idpartido,
#             user_data.email_usuario,
#             user_data.usuario_administrador,
#             user_data.idcamara,
#             user_data.foto_perfil,
#             user_data.usuario_presidente
#             )
#
#         msg = {
#             "message": "Usuario criado com sucesso",
#             **user_data.dict()
#             }
#         return JSONResponse(status_code=status.HTTP_201_CREATED, content=msg)
#
#     except Exception as error:
#
#         msg = {"message": error}
#         print(msg)
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))