from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()
database = []  # Provisório para testes


# 'response_model' será reponsável por sempre retornar um valor do tipo Message
# Message foi definido no schemas para padronizar o tipo de contrato da chamada
@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}


@app.get('/olamundo/', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def olamundo():
    return """
    <html>
        <head>
            <title>Olá Mundo HTML</title>
        </head>
        <body>
            <h1>Olá, Mundo!</h1>
        </body>
    </html>"""


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(
        # Desempacota o dict e preenche novamente sem precisar setar manual
        **user.model_dump(),
        id=len(database) + 1,  # teste
    )

    database.append(user_with_id)

    return user_with_id


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}


@app.get(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def read_user_by_id(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Usuário não encontrado!',
        )

    return database[user_id - 1]


# PUT - Para que haja update, é necessário enviar todos os dados
@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(user_id: int, user: UserSchema):
    user_with_id = UserDB(
        **user.model_dump(),
        id=user_id,
    )
    if user_id < 1 or user_id > len(database):
        # Exception para caso não encontre o usuário
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Usuário não encontrado!',
        )

    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Usuário não encontrado!',
        )
    return database.pop(user_id - 1)
