from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
from .mascotas import Mascota

class Adquisicion:
    def __init__(self, data):
        self.edad_adopcion = data['edad_adopcion']
        self.donde_adquisicion = data['donde_adquisicion']
        self.tiempo_con_madre_hnos = data['tiempo_con_madre_hnos']
        self.momento_salida_a_calle = data['momento_salida_a_calle']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_adquisicion(form):
        #Aquí recibe el request.form
        is_valid = True

        if form["edad_adopcion"] == "":
            is_valid = False
            flash("Ingrese un estimado de la edad en que adopto a su mascota", "form_adquisicion")

        if len(form['donde_adquisicion']) < 3:
            is_valid = False
            flash("Ingrese desde dónde adquirió a su mascota", "form_adquisicion")

        if len(form['tiempo_con_madre_hnos']) < 3:
            is_valid = False
            flash("Ingrese hasta qué edad su mascota estuvo con su madre/hermanos", "form_adquisicion")

        if len(form['momento_salida_a_calle']) < 3:
            is_valid = False
            flash("Ingrese a qué edad su mascota salió a la calle", "form_adquisicion")

        return is_valid
    
    @classmethod
    def save(cls, form):
        query = "INSERT INTO adquisiciones (edad_adopcion, donde_adquisicion, tiempo_con_madre_hnos, momento_salida_a_calle) VALUES (%(edad_adopcion)s, %(donde_adquisicion)s, %(tiempo_con_madre_hnos)s, %(momento_salida_a_calle)s"
        result = connectToMySQL('esquema_etologia').query_db(query, form) #como respuesta me traerá el ID del registro que se acaba de crear 
        return result
        