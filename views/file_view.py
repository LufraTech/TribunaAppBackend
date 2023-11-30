from fastapi import APIRouter, HTTPException, Response, status
from schemas.file import File
from services.file_service import FileRepository
from fastapi.responses import JSONResponse

route_file = APIRouter(prefix='/file', tags=['Arquivo'])

@route_file.post('/create')
async def create_user(file_data: File):

    # email_db = await CreateUser.check_email(user_input.email)
    # if email_db != []:
    #     msg = {"message": f"Email: {user_input.email} já cadastrado"}
    #     return JSONResponse(content=msg, status_code=409)

    try:

        await FileRepository.create_file(
            file_data.nome_arquivo,
            file_data.idsessao,
            )

        msg = {
            "message": "arquivo criado com sucesso",
            "nome_arquivo": file_data.nome_arquivo,
            "idsessao": file_data.idsessao,
            }
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=msg)

    except Exception as error:

        msg = {"message": error}
        print(msg)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))

# @route_file.post('/create')
# async def create(file_data: File):
#     try:
#         return JSONResponse(status_code=status.HTTP_201_CREATED, content=await FileRepository.create(file_data))
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))