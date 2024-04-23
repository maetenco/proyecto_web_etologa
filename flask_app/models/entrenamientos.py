from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
from .mascotas import Mascota

class Entrenamiento:
    def __init__(self, data):
        self.tuvo_entrenamiento = data['tuvo_ entrenamiento']
        self.motivo_entrenamiento = data['motivo_entrenamiento']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_entrenamiento(form):
        #Aquí recibe el request.form
        is_valid = True

        if len(form['motivo_entrenamiento']) < 3:
            is_valid = False
            flash("Ingrese el motivo de entrenamiento a su mascota", "form_entrenamiento")


        return is_valid
    
    @classmethod
    def save(cls, form):
        query = "INSERT INTO entrenamientos (tuvo_entrenamiento, motivo_entrenamiento) VALUES (%(tuvo_entrenamiento)s, %(motivo_entrenamiento)s)"
        result = connectToMySQL('esquema_etologia').query_db(query, form) #como respuesta me traerá el ID del registro que se acaba de crear 
        return result
        