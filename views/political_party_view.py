from fastapi import APIRouter, HTTPException, Response, status

from schemas.politicalparty import PoliticalParty
from services.political_party_service import PoliticalPartyRepository
from fastapi.responses import JSONResponse

route_political_party = APIRouter(prefix='/party', tags=['Partido'])


@route_political_party.post('/create')
async def create_user(political_data: PoliticalParty):

    # email_db = await CreateUser.check_email(user_input.email)
    # if email_db != []:
    #     msg = {"message": f"Email: {user_input.email} já cadastrado"}
    #     return JSONResponse(content=msg, status_code=409)

    try:
        await PoliticalPartyRepository.create_political_party(political_data)

        msg = {
            "message": "Partido criado com sucesso",
            "nome_partido": political_data.nome_partido,
            "sigla_partido": political_data.sigla_partido,
            "deferimento": political_data.deferimento,
            "presidente_nacional": political_data.presidente_nacional,
            "numero_legenda": political_data.numero_legenda
            }
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=msg)

    except Exception as error:

        msg = {"message": error}
        print(msg)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))

# @router_political_party.post('/create')
# async def create(political_party_data: PoliticalParty):
#     try:
#         return JSONResponse(status_code=status.HTTP_201_CREATED, content=await PoliticalPartyRepository.create(political_party_data))
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))