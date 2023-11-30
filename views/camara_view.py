from fastapi import APIRouter, HTTPException, Response, status
from schemas.camara import Camara
from services.camara_service import CamaraRepository
from fastapi.responses import JSONResponse

route_camara = APIRouter(prefix='/camara', tags=['Camara'])


@route_camara.post('/create')
async def create(camara_data: Camara):
    try:
        await CamaraRepository.create_camara(camara_data)
        message = {
            "message": 'Camara Criada',
            "nome_camara": camara_data.nome_camara,
            "foto_camara": camara_data.foto_camara,
            "cep": camara_data.cep
        }
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=message)


    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@route_camara.put('/update/{idcamara}')
async def update(idcamara: int, camara_data: Camara):
    try:
        await CamaraRepository.update_camara(camara_data.nome_camara, camara_data.idcidade, camara_data.foto_camara,
                                             camara_data.cep)
        message = {
            "message": 'Atualizado'
        }
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=message)

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


# @route_camara.get('/getall')
# async def get_all():
#     try:
#         return JSONResponse(status_code=status.HTTP_201_CREATED, content=await CamaraRepository.get_all())
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@route_camara.delete('/delete/{idcamara}')
async def delete(idcamara: int):
    print("Sua mae")
    try:
        await CamaraRepository.delete_camara(idcamara)
        message = {
            "message": 'Deletado'
        }
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=message)

    except Exception as e:

        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
