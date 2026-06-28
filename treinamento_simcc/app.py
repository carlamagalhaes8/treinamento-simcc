from flask import Flask

from rest.rest_pesquisador import rest_pesquisador
from rest.rest_producao import rest_producao

app = Flask(__name__)

app.register_blueprint(
    rest_pesquisador
)

app.register_blueprint(
    rest_producao
)