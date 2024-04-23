from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
from .mascotas import Mascota

class Vacuna:
    def __init__(self, data):
        self.nom_fecha_ultim_vac = data['nom_fecha_ultima_vac']
        self.nom_fecha_antipar = data['nom_fecha_antiparasitario']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_vacuna(form):
        #Aquí recibe el request.form
        is_valid = True

        if len(form['nom_fecha_ult_vac']) < 3:
            is_valid = False
            flash("Nombre y fecha de la última vacuna", "form_vacunas")

        if len(form['nom_fecha_antiparasitario']) < 3:
            is_valid = False
            flash("Nombre y fecha del último antiparasitario", "form_vacunas")

        return is_valid
    
    @classmethod
    def save(cls, form):
        query = "INSERT INTO vacunas (nom_fecha_ultim_vac, nom_fecha_antipar) VALUES (%(nom_fecha_ultim_vac)s, %(nom_fecha_antipar)s"
        result = connectToMySQL('esquema_etologia').query_db(query, form) #como respuesta me traerá el ID del registro que se acaba de crear 
        return result
        