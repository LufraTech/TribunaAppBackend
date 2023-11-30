from fastapi import FastAPI
from config import db
import uvicorn
from views.file_view import route_file
from views.camara_view import route_camara
from views.political_party_view import route_political_party
from views.session_view import route_session
from views.user_view import route_user
from views.city_view import route_city
from views.state_view import route_state
from views.auth import router_auth


def init_app():
    app = FastAPI(
        title='Tn Consig',
        description="API for Tn Consig",
        version="1.0.0"
    )
    app.include_router(router=route_user)
    app.include_router(router=route_camara)
    app.include_router(router=route_political_party)
    app.include_router(router=route_session)
    app.include_router(router=route_file)
    app.include_router(router=route_city)
    app.include_router(router=route_state)
    # app.include_router(router=route_login)
    app.include_router(router=router_auth)


    @app.on_event("startup")
    async def startup():
        await db.create_all()
    @app.on_event("shutdown")
    async def shutdown():
        await db.close()
    @app.get("/")
    async def home():
        return {"VAI SE FUDER EU SOU FODA"}

    return app

app= init_app()

if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8000, reload=False)
