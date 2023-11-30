from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    email_usuario: str
    senha_usuario: str

class Token(BaseModel):
    access_token: str
    token_type: str
