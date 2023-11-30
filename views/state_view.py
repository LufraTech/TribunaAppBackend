from fastapi import APIRouter, HTTPException, status
from services.state_service import StateRepository
from fastapi.responses import JSONResponse
from schemas.state import State

route_state = APIRouter(prefix='/state', tags=['State'])

@route_state.post('/create')
async def create_state(state_data: State):
    try:
        print(state_data)
        await StateRepository.create_state(state_data)

        msg = {
            "message": "Estado criado com sucesso",
            "nome_estado": state_data.nome_estado,
            }
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=msg)
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))


@route_state.get('/getallstates')
async def get_all_states():

    states = await StateRepository.get_all_state()
    states_list = [{"nome_estado": state[0]} for state in states]

    try:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=states_list)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))