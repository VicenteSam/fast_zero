from pydantic import BaseModel


# Schema que padroniza o retorno da API.
# O retorno será sempre uma mensagem com corpo String
# Necessariamente tem que ser uma variável 'message'
class Message(BaseModel):
    message: str
