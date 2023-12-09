from fastapi import APIRouter, HTTPException, Response, status
from schemas.session import Session
from services.session_service import SessionRepository
from fastapi.responses import JSONResponse
from services.user_session_service import UserSessionRepository
from schemas.user_session import UserSession

route_session = APIRouter(prefix='/session', tags=['Sessao'])


@route_session.post('/create')
async def create(session_data: Session):
    try:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=await SessionRepository.create(session_data))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@route_session.get('/getallbysession/{idsessao}')
async def get_all_by_session(idsessao: int):
    try:
        usuarios_sessao = await SessionRepository.get_users_session(idsessao)
        print(usuarios_sessao)
        usuarios_list = [
            {"nome_usuario": user[1],
             "email_usuario": user[2],
             "foto_perfil": user[4],
             "idpartido": user[5],
             "idcamara": user[6],
             "usuario_administrador": user[7],
             "usuario_presidente": user[8]}
            for user in usuarios_sessao]
        return JSONResponse(status_code=status.HTTP_200_OK, content=usuarios_list)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@route_session.post('/enter_session')
async def enter_session(user_session_data: UserSession):
    try:
        await SessionRepository.enter_session(user_session_data)
        msg = {
            "message": f"Usuario {user_session_data.idusuario} entrou na sessão",
            }
        return JSONResponse(status_code=status.HTTP_200_OK, content=msg)
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))
