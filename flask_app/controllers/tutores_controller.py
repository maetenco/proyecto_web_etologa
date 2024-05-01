#importaciones
from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app


#importacion de todos los modelos
from flask_app.models.mascotas import Mascota
from flask_app.models.tutores import Tutor
from flask_app.models.pre_consultas import Pre_consulta
from flask_app.models.veterinarios import Veterinario

from flask_app.models.antecedentes import Antecedente
from flask_app.models.adquisiciones import Adquisicion
from flask_app.models.vacunas import Vacuna
from flask_app.models.castraciones import Castracion
from flask_app.models.alimentaciones import Alimentacion
from flask_app.models.entrenamientos import Entrenamiento
from flask_app.models.diagnosticos_previos import Diagnostico_previo

from flask_app.models.examenes import Examen
from flask_app.models.derivaciones import Derivacion

from flask_app.models.motivos import Motivo

#Para subir archivo tipo foto al servidor
from werkzeug.utils import secure_filename 
import os


#Importo bcrypt que es el que me escripta las contraseñas
from flask_bcrypt import Bcrypt

#ahora lo inicializo
bcrypt = Bcrypt(app)


@app.route("/tutores")
def tutores():
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
    
    mascotas = Antecedente.get_mascota(form)

    return render_template("dashboard_tutor.html", tutor=tutor, mascotas=mascotas)


@app.route('/pre_consulta')
def pre_consulta():
    if 'tutor_id' not in session:
        return redirect('/')
    
    return render_template("pre_consultaPRO.html")


@app.route('/guardar_datos', methods=['POST'])
def guardar_datos():

    if 'tutor_id' not in session:
        return redirect('/')

    print("guardar_datos1")

    #Nueva mascota:
    nueva_mascota= {'nombre': request.form['nombre_mas'],
                    'tutor_id': session['tutor_id'], 
                    'veterinario_id': '1', 
                    }
    
    mascota_id = Mascota.save(nueva_mascota)

    print(mascota_id)
    
    print("guardar_datos2")

    Antecedente.save(request.form,mascota_id)
    Adquisicion.save(request.form,mascota_id)
    Vacuna.save(request.form,mascota_id)
    Castracion.save(request.form,mascota_id)
    Alimentacion.save(request.form,mascota_id)
    Entrenamiento.save(request.form,mascota_id)
    Diagnostico_previo.save(request.form,mascota_id)
    Examen.save(request.form,mascota_id)
    Derivacion.save(request.form,mascota_id)
    Motivo.save(request.form,mascota_id)

    return redirect ("/dashboard_tutor")


@app.route('/registrar-archivo', methods=['GET', 'POST'])
def registarArchivo():
    if request.method == 'POST':

        #Script para archivo
        file     = request.files['archivo']
        basepath = os.path.dirname (__file__) #La ruta donde se encuentra el archivo actual
        filename = secure_filename(file.filename) #Nombre original del archivo
        
        #capturando extensión del archivo ejemplo: (.png, .jpg, .pdf ...etc)
        extension           = os.path.splitext(filename)[1]
        nuevoNombreFile     = stringAleatorio() + extension
    
        upload_path = os.path.join (basepath, 'static/archivos', nuevoNombreFile) 
        file.save(upload_path)
        
        return '<br><br><center>El Registro fue un Exito &#x270c;&#xfe0f; </center>'
    return render_template('index.html')

@app.route('/editar/mascota/<int:id>') 
def editar_cita(id):
    if 'tutor_id' not in session:
        return redirect('/')
    
    diccionario = {"id": id}

    m = Mascota.obtener_mascota(diccionario)
    return render_template('editar_preconsulta.html', m=m)

    
@app.route('/delete/mascota/<int:id>')
def delete_mascotas(id):
    if 'tutor_id' not in session:
        return redirect('/')

    form = {"id": id}


    Adquisicion.delete(form)
    Alimentacion.delete(form)
    Antecedente.delete(form)
    Castracion.delete(form)
    Derivacion.delete(form)
    Diagnostico_previo.delete(form)
    Entrenamiento.delete(form)
    Examen.delete(form)
    Motivo.delete(form)
    Vacuna.delete(form)

    Mascota.delete(form)
    
    return redirect("/dashboard_tutor")
