from pydantic import BaseModel

class User(BaseModel):

    primeiro_nome: str
    sobrenome: str
    senha_usuario: str
    email_usuario: str
    foto_perfil: str | None = None
    idpartido: int
    usuario_presidente: bool
    usuario_vereador: bool
    usuario_administrador: bool
    idcamara: int
    status: bool | None = None


