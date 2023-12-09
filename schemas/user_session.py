from pydantic import BaseModel


class UserSession(BaseModel):

    idusuario: str
    idsessao: str

