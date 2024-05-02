from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
from .mascotas import Mascota

class Alimentacion:
    def __init__(self, data):
        self.tipo_alimentacion = data['tipo_alimentacion']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.mascota_id = data['mascota_id']

    @staticmethod
    def validate_alimentacion(form):
        #Aquí recibe el request.form
        is_valid = True

        if len(form['tipo_alimentacion']) < 3:
            is_valid = False
            flash("Ingrese el tipo de alimentación de su mascota", "form_adquisicion")

        return is_valid
    
    @classmethod
    def save(cls, form,mascota):

        nuevo_form= {'tipo_alimentacion': form['tipo_alimentacion'],
                    'mascota_id': mascota,
                    }
        
        query = "INSERT INTO alimentaciones (tipo_alimentacion,mascota_id) VALUES (%(tipo_alimentacion)s,%(mascota_id)s)"
        result = connectToMySQL('esquema_etologia').query_db(query, nuevo_form) #como respuesta me traerá el ID del registro que se acaba de crear 
        return result
    
    @classmethod
    def update(cls, form):
        query = "UPDATE alimentaciones SET tipo_alimentacion=%(tipo_alimentacion)s WHERE mascota_id=%(mascota_id)s" 
        result = connectToMySQL('esquema_etologia').query_db(query, form)
        return result

    @classmethod
    def delete(cls,form):
        query = "DELETE FROM alimentaciones WHERE mascota_id = %(id)s"
        result = connectToMySQL('esquema_etologia').query_db(query, form)
        return result    