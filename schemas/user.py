from pydantic import BaseModel

class User(BaseModel):

    nome_usuario: str
    senha_usuario: str
    email_usuario: str
    foto_perfil: str
    idpartido: int
    usuario_presidente: bool
    vereador: bool
    usuario_administrador: bool
    idcamara: int