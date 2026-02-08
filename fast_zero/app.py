from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


# 'response_model' será reponsável por sempre retornar um valor do tipo Message
# Message foi definido no schemas para padronizar o tipo de contrato da chamada
@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}


@app.get('/olamundo', status_code=HTTPStatus.OK, response_class=HTMLResponse)
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
