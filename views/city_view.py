from fastapi import APIRouter, HTTPException, Response, status
from schemas.city import City
from fastapi.responses import JSONResponse
from services.city_service import CityRepository

route_city = APIRouter(prefix='/city', tags=['City'])

@route_city.post('/create')
async def create_city(city_data: City):
    try:
        await CityRepository.create_city(
            city_data.nome_cidade,
            city_data.idestado,
            )
        msg = {
            "message": "Cidade criada com sucesso",
            "nome_cidade": city_data.nome_cidade,
            "idestado": city_data.idestado,
            }
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=msg)

    except Exception as error:

        msg = {"message": error}
        print(msg)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))

@route_city.get('/getallcities')
async def get_all_cities():
    cities = await CityRepository.get_all_city()

    cities_list = [{"nome_cidade": city[0], "idestado": city[1]} for city in cities]
    try:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=cities_list)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@route_city.delete('/delete/{idcity}')
async def delete_city(idcity: int):
    try:
        await CityRepository.delete_city(idcity)
        msg = {
            "message": "Cidade deletada com sucesso",
            }
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=msg)

    except Exception as error:

        msg = {"message": error}
        print(msg)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))

@route_city.put('/update/{idcidade}')
async def update_city(city_data: City,idcidade: int):
    try:
        await CityRepository.update_city(nome_cidade=city_data.nome_cidade, idcidade= idcidade)
        msg = {
            "message": "Cidade atualizada com sucesso",
            }
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=msg)

    except Exception as error:

        msg = {"message": error}
        print(msg)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(msg))