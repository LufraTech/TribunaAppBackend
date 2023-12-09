from pydantic import BaseModel


class UserSession(BaseModel):

    idusuariosessao: int | None = None
    idusuario: str
    idsessao: str

