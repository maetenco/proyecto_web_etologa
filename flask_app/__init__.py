#importar flask
from flask import Flask

#inicializar la app
app = Flask(__name__)

#llave secreta
app.secret_key = "llavesita secret top"


app.config['UPLOAD_FOLDER'] = "flask_app/static/archivo/examenes"
app.config['UPLOAD_FOLDER2'] = "flask_app/static/archivo/derivaciones"
