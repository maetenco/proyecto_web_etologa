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
from flask_app.models.alimentaciones import Alimentacion
from flask_app.models.castraciones import Castracion
from flask_app.models.derivaciones import Derivacion
from flask_app.models.diagnosticos_previos import Diagnostico_previo
from flask_app.models.entrenamientos import Entrenamiento
from flask_app.models.examenes import Examen
from flask_app.models.motivos import Motivo
from flask_app.models.vacunas import Vacuna

#Importo bcrypt que es el que me escripta las contraseñas
from flask_bcrypt import Bcrypt

#ahora lo inicializo
bcrypt = Bcrypt(app)

@app.route('/veterinario') 
def veterinario():
    return render_template('veterinario.html')

@app.route('/register_vet', methods=['POST'])
def register_vet():
    #primero valido que la información sea correcta:
    if not Veterinario.validate_veterinario(request.form):
        return redirect ("/veterinario")
    
    #Aquí encripto la contraseña ---> Aquí la profe subio para importar bcrypt e inicializarlo 
    pass_encrypt = bcrypt.generate_password_hash(request.form['password'])  
    #Con esto tengo la contraseña encriptada
    form = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pass_encrypt
    }   #entonces aquí si agrego la contraseña ya encriptada  

    #debo verificar el inicio de sesión
    nuevo_veterinario_id = Veterinario.save(form) #recibo el ID del nuevo Usuario 
    session['veterinario_id'] = nuevo_veterinario_id #Entonces guardo el nuevo_id para que la persona que esté iniciando sesión, ya haya iniciado sesión.
    return redirect('/veterinario')


@app.route('/login_vet', methods=['POST'])
def login_vet():
    veterinario = Veterinario.get_by_email(request.form) #Aquí puede ser que --> user = instancia User ó False. Es la instancia cuando si hay existe un usuario con ese correo o es False cuando no existe ese correo.

    if not veterinario:
        flash("E-mail no registrado", "login_vet")
        return redirect('/veterinario')
    
    #si user SI es instancia de User, entonces debería verificar la contraseña
    if not bcrypt.check_password_hash(veterinario.password, request.form['password']):
        flash("Password incorrecto", "login_vet")
        return redirect('/veterinario')
    
    session['veterinario_id'] = veterinario.id #ESto es si todo está bien, quiere decir que guardo el id del usuario y luego redirijo a recipes
    return redirect('/dashboard_vet')


@app.route('/dashboard_vet')
def dashboard_vet():
    if 'veterinario_id' not in session:
        return redirect ("/")
    
    form = {"id": session['veterinario_id']}
    veterinario = Veterinario.get_by_id_vet(form)
    
    mascotas = Mascota.ver_mascotas()

    if len(mascotas) == 0:
        mascotas=[]

    return render_template("dashboard_vet.html", veterinario=veterinario, mascotas=mascotas)

@app.route('/show/<int:id>')
def ver_mascota(id):
    if 'veterinario_id' not in session:
        return redirect ("/")
    
    form = {"id": session['veterinario_id']}
    diccionario = {"id": id}
    veterinario = Veterinario.get_by_id_vet(form)

    m = Mascota.obtener_mascota(diccionario)  


    return render_template("ver_mascota.html",m=m)

@app.route('/edit/<int:id>') 
def editar_cita(id):
    if 'veterinario_id' not in session:
        return redirect('/')
    
    diccionario = {"id": id}

    m = Mascota.obtener_mascota(diccionario)
    return render_template('editar_preconsulta.html', m=m)

@app.route('/delete/<int:id>')
def delete_mascota(id):
    if 'veterinario_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    #Borrar
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
    
    return redirect("/dashboard_vet")

    


@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")



#FLUJO --> Creo una ruta de registro a través del método de POST que va a recibir el request.form con toda la información que ingresó el usuario, luego valido que esa información sea correcta y si no es válida lo regreso al index.html (a la pantalla principal para que corrija sus errores. 
#Si todo está bien entonces encripto la contraseña y creo un nuevo diccionario con toda la información, incluyendo la contraseña pero ya encriptada), guardo el usuario. Obtengo de vuelta el nuevo ID del usuario que se acaba de registrar, para guardar ese ID en la sesión(session) y al final redirigir hacia una pantalla nueva que se llame "recipes", y esa pantalla sólo será accedida por aquellos que ya se registraron y tienen su sesión iniciada
"""



"""