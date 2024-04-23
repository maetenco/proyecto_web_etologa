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
    def save(cls, form):
        query = "INSERT INTO castraciones (castracion, fecha_castracion, motivo_castracion) VALUES (%(castracion)s, %(motivo_castracion)s, %(motivo_castracion)s"
        result = connectToMySQL('esquema_etologia').query_db(query, form) #como respuesta me traerá el ID del registro que se acaba de crear 
        return result
        