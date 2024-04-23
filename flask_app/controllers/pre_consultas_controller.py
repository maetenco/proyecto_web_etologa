#importaciones
from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app

#importacion de todos los modelos
from flask_app.models.mascotas import Mascota
from flask_app.models.tutores import Tutor
from flask_app.models.pre_consultas import Pre_consulta
from flask_app.models.veterinarios import Veterinario

#Importo bcrypt que es el que me escripta las contraseñas
from flask_bcrypt import Bcrypt

#ahora lo inicializo
bcrypt = Bcrypt(app)
"""
@app.route("/")
def ():
    return render_template("pre_consulta.html")

"""