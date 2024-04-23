#importaciones
from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app

from random import sample
from werkzeug.utils import secure_filename 
import os

#importacion de todos los modelos
from flask_app.models.mascotas import Mascota
from flask_app.models.tutores import Tutor
from flask_app.models.pre_consultas import Pre_consulta
from flask_app.models.veterinarios import Veterinario
from flask_app.models.antecedentes import Antecedente
from flask_app.models.adquisiciones import Adquisicion
from flask_app.models.vacunas import Vacuna


#Importo bcrypt que es el que me escripta las contraseñas
from flask_bcrypt import Bcrypt

#ahora lo inicializo
bcrypt = Bcrypt(app)


@app.route("/tutores")
def nuevo_tutor():
    return render_template("tutores.html")

@app.route("/create_tutor", methods=['POST'])
def register_tutor():
    if not Tutor.validate_tutor(request.form):
        return redirect('/tutores#register-form')
    
    pass_encrypt = bcrypt.generate_password_hash(request.form['password'])
    form = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"],
        "password": pass_encrypt
    }
    nuevo_tutor_id = Tutor.save_tutor(form)
    flash("Usuario guardado correctamente", "exito")
    session['tutor_id'] = nuevo_tutor_id
    return redirect('/tutores#register-form')

@app.route('/login_tutor', methods=['POST'])
def login_tutor():
    tutor = Tutor.get_by_email_tutor(request.form)
    if not tutor:
        flash("E-mail no registrado", "login_tutor")
        return redirect('/tutores#login-form')

    if not bcrypt.check_password_hash(tutor.password, request.form['password']):
        flash("Password incorrecto", "login_tutor")
        return redirect('/tutores#login-form')
    
    session['tutor_id'] = tutor.id 
    return redirect('/dashboard_tutor')

@app.route('/dashboard_tutor')
def dashboard_tutor():
    if 'tutor_id' not in session:
        return redirect('/')
    
    form = {"id": session['tutor_id']}
    tutor = Tutor.get_by_id_tutor(form)
    
    #mascotas = Mascota.get_all_mascotas()

    return render_template("dashboard_tutor.html", tutor=tutor)#mascotas=mascotas


@app.route('/pre_consulta')
def pre_consulta():
    if 'tutor_id' not in session:
        return redirect('/')
    
    return render_template("pre_consulta.html")

#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    return 'Ruta no encontrada'

def stringAleatorio():
    #Generando string aleatorio
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud         = 20
    secuencia        = string_aleatorio.upper()
    resultado_aleatorio  = sample(secuencia, longitud)
    string_aleatorio     = "".join(resultado_aleatorio)
    return string_aleatorio
@app.route('/guardar_datos', methods=['POST', 'GET'])
def guardar_datos():
    if 'tutor_id' not in session:
        return redirect('/')
    
    """GUARDAR ARCHIVOS"""
    if request.method == 'POST':
    
        nombre_mas = request.form['nombre_mas']
        dog_or_cat = request.form['dog_or_cat']
        raza = request.form['raza']
        fecha_nac = request.form['fecha_nac']
        edad = request.form['edad']
        peso = request.form['peso']
        sexo = request.form['sexo']
        edad_adopcion = request.form['edad_adopcion']
        donde_adquisicion = request.form['donde_adquisicion']
        tiempo_con_madre_hrnos = request.form['tiempo_con_madre_hrnos']
        momento_salida_a_calle = request.form['momento_salida_a_calle']

        Antecedente.save(request.form)


        #Script para archivo
        file     = request.files['archivo']
        basepath = os.path.dirname (__file__) #La ruta donde se encuentra el archivo actual
        filename = secure_filename(file.filename) #Nombre original del archivo
        
        #capturando extensión del archivo ejemplo: (.png, .jpg, .pdf ...etc)
        extension           = os.path.splitext(filename)[1]
        nuevoNombreFile     = stringAleatorio() + extension

        upload_path = os.path.join (basepath, 'static/archivos', nuevoNombreFile) 
        file.save(upload_path)



    print(f"nombre mascota: {nombre_mas}, perro o gato: {dog_or_cat}, raza: {raza}, fecha_nac: {fecha_nac}, edad: {edad}, peso:{peso}, sexo: {sexo}, edad_adopcion: {edad_adopcion}, donde_adquisicion: {donde_adquisicion}, tiempo_con_madre_hrnos: {tiempo_con_madre_hrnos}, momento_salida_a_calle: {momento_salida_a_calle} ")
    """
    if not Antecedente.validate_antecedentes(request.form):
        return redirect("pre_consulta")
    Antecedente.save(request.form)

    if not Adquisicion.validate_adquisicion(request.form):
        return redirect("pre_consulta")
    Adquisicion.save(request.form)

    if not Vacuna.validate_vacuna(request.form):
        return redirect("pre_consulta")
    Vacuna.save(request.form)

    """
    return "Formulario enviado exitosamente"

