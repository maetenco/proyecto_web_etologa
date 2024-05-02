from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
from .mascotas import Mascota

class Castracion:
    def __init__(self, data):
        self.castracion = data['castracion']
        self.fecha_castracion = data['fecha_castracion']
        self.motivo_castracion = data['motivo_castracion']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.mascota_id = data['mascota_id']


    @staticmethod
    def validate_castracion(form):
        #Aquí recibe el request.form
        is_valid = True

        if form["fecha_castracion"] == "":
            is_valid = False
            flash("Ingrese una fecha de castración", "form_castracion")

        if len(form['motivo_castracion']) < 3:
            is_valid = False
            flash("Ingrese el motivo de la castración", "form_adquisicion")
        return is_valid
    
    @classmethod
    def save(cls, form,mascota):

        nuevo_form= {'castracion': form['castracion'],
                    'fecha_castracion': form['fecha_castracion'], 
                    'motivo_castracion': form['motivo_castracion'], 
                    'mascota_id': mascota,                     
                    }

        query = "INSERT INTO castraciones (castracion, fecha_castracion, motivo_castracion, mascota_id) VALUES (%(castracion)s, %(fecha_castracion)s, %(motivo_castracion)s, %(mascota_id)s)"
        result = connectToMySQL('esquema_etologia').query_db(query, nuevo_form) #como respuesta me traerá el ID del registro que se acaba de crear 
        return result
        
    @classmethod
    def update(cls, form):
        query = "UPDATE castraciones SET castracion=%(castracion)s, fecha_castracion=%(fecha_castracion)s, motivo_castracion=%(motivo_castracion)s WHERE mascota_id=%(mascota_id)s" 
        result = connectToMySQL('esquema_etologia').query_db(query, form)
        return result
    
    @classmethod
    def delete(cls,form):
        query = "DELETE FROM castraciones WHERE mascota_id = %(id)s"
        result = connectToMySQL('esquema_etologia').query_db(query, form)
        return result    