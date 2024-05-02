#importaciones
from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app
from datetime import datetime 
from flask import jsonify

#importacion de todos los modelos
from flask_app.models.mascotas import Mascota
from flask_app.models.tutores import Tutor
from flask_app.models.pre_consultas import Pre_consulta
from flask_app.models.veterinarios import Veterinario
from flask_app.models.agenda import Agenda

#Importo bcrypt que es el que me escripta las contraseñas
from flask_bcrypt import Bcrypt

#ahora lo inicializo
bcrypt = Bcrypt(app)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/noticias')
def noticias():
    return render_template("noticias.html")

@app.route('/agenda')
def agenda():
    eventos = Agenda.get_all()
    return render_template("agenda.html", agenda=eventos, now=datetime.now,agno=datetime.year)
    

@app.route('/blog')
def blog():
    return render_template("blog.html")

@app.route('/preguntas_frecuentes')
def preguntas_frecuentes():
    return render_template("preguntas_frecuentes.html")

@app.route('/sobre_mi')
def sobre_mi():
    return render_template("sobre_mi.html")

