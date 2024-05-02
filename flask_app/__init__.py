#importar flask
from flask import Flask

#inicializar la app
app = Flask(__name__)

#llave secreta
app.secret_key = "llavesita secret top"
