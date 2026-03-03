from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI(title='Teste de Api!')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Ola Mundo!'}


@app.get('/HTML', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def HTML():
    return """
    <html>
        <head>
            <title> Nosso ola Mundo!</title>
        </head>
        <body>
            <h1> Ola Mundo </h1>
        </body>
    </html>"""
