from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
from .mascotas import Mascota

class Motivo:
    def __init__(self, data):
        self.motivo_consulta = data['motivo_consulta']
        self.otra_mascota = data['otra_mascota']
        self.derivacion = data['derivacion']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_motivos(form):
        #Aquí recibe el request.form
        is_valid = True

        if len(form['motivo_consulta']) < 3:
            is_valid = False
            flash("Explique el motivo de su consulta", "form_diagnostico_previo")

        if len(form['otra_mascota']) < 3:
            is_valid = False
            flash("Por favor ingrese los nombres y edades de las mascotas que convivan en su hogar", "form_diagnostico_previo")

        return is_valid
    
    @classmethod
    def save(cls, form):
        query = "INSERT INTO motivos (motivo_consulta, otra_mascota, derivacion) VALUES (%(motivo_consulta)s, %(otra_mascota)s, %(derivacion)s)"
        result = connectToMySQL('esquema_etologia').query_db(query, form) #como respuesta me traerá el ID del registro que se acaba de crear 
        return result
        