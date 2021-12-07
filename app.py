from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec

server = Flask(__name__)

spec = FlaskPydanticSpec('flask', title='Live de Python')
spec.register(server)


@server.get('/pessoas')
def pegar_pessoas():
    return 'Programaticamente Falando'


server.run()
