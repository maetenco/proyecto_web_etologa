from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #Patrón de email

class Tutor:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_tutor(form):
        is_valid = True
        
        if len(form['nombre']) < 2:
            flash('El nombre del tutor debe tener al menos 2 caracteres', "registro_tutor")
            is_valid = False
        
        if len(form['apellido']) < 2:
            flash('El apellido del tutor debe tener al menos 2 caracteres', "registro_tutor")
            is_valid = False

        if not EMAIL_REGEX.match(form['email']):
            flash('E-email es inválido', "registro_tutor")
            is_valid = False

        query = "SELECT * FROM tutores WHERE email = %(email)s"
        results = connectToMySQL('esquema_etologia').query_db(query, form)
        if len(results) >= 1:
            flash('E-email registrado previamente', "registro_tutor")
            is_valid = False
        
        if len(form['password']) < 6:
            flash('Su contraseña debe tener al menos 6 caracteres', "registro_tutor")
            is_valid = False

        if form['password'] != form['confirma']:
            flash('Las contraseñas no coinciden', "registro_tutor")
            is_valid = False

        return is_valid

    @classmethod
    def save_tutor(cls, form):
        query = "INSERT INTO tutores (nombre, apellido, email, password) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s)"
        result = connectToMySQL('esquema_etologia').query_db(query, form)
        return result 

    @classmethod
    def get_by_id_tutor(cls, form):
        #form = {"id": 1}
        query = "SELECT * FROM tutores WHERE id = %(id)s"
        result = connectToMySQL('esquema_etologia').query_db(query, form)
        #Esto me regresa una lista de diccionarios que sólo tiene una posición
        tutor = cls(result[0])
        return tutor
    
    @classmethod
    def get_by_email_tutor(cls, form): #recibo el formulario que será un diccionario que tiene el email que busco que también incluye el password ---->  form = {"email": "elena@codingdojo.com", "password": "Elenita"}
        query = "SELECT * FROM tutores WHERE email = %(email)s"
        results = connectToMySQL('esquema_etologia').query_db(query, form)
        if len(results) == 1:
            #si existe el usuario, me regresa sólo UN registro y tiene la posición cero [0]
            tutor = cls(results[0])
            return tutor #Entonces regreso la instancia del usuario con ese correo
        else:
            return False
        
    @classmethod
    def get_by_email_tutor(cls, form): #recibo el formulario que será un diccionario que tiene el email que busco que también incluye el password ---->  form = {"email": "elena@codingdojo.com", "password": "Elenita"}
        query = "SELECT * FROM tutores WHERE email = %(email)s"
        results = connectToMySQL('esquema_etologia').query_db(query, form)
        if len(results) == 1:
            #si existe el usuario, me regresa sólo UN registro y tiene la posición cero [0]
            tutor = cls(results[0])
            return tutor #Entonces regreso la instancia del usuario con ese correo
        else:
            return False