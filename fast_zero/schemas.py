# BaseModel utiliza tipos primitivos
# EmailStr utiliza um tipo específico de String para Emails
from pydantic import BaseModel, EmailStr


# Schema que padroniza o retorno da API.
# O retorno será sempre uma mensagem com corpo String
# Necessariamente tem que ser uma variável 'message'
class Message(BaseModel):
    message: str


# Schema para padronizar as informações do usuário
class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


# Schema para retornar apenas oque deve ser retornado
class UserPublic(BaseModel):
    id: int
    username: str
    email: str


# Herança de classes - UserDB (filho) herda de UserSchema (mãe)
# Todos os campos de UserSchema estarão no UserDB + id
class UserDB(UserSchema):
    id: int


# Schema para retornar lista de usuários
class UserList(BaseModel):
    users: list[UserPublic]
