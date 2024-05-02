from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
from .mascotas import Mascota

class Vacuna:
    def __init__(self, data):
        self.nom_fecha_ultima_vac = data['nom_fecha_ultima_vac']
        self.nom_fecha_antiparasitario = data['nom_fecha_antiparasitario']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.mascota_id = data['mascota_id']

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
    def save(cls, form,mascota):

        nuevo_form= {'nom_fecha_ultima_vac': form['nom_fecha_ultima_vac'],
                    'nom_fecha_antiparasitario': form['nom_fecha_antiparasitario'], 
                    'mascota_id': mascota,                     
                    }

        query = "INSERT INTO vacunas (nom_fecha_ultima_vac, nom_fecha_antiparasitario,mascota_id) VALUES (%(nom_fecha_ultima_vac)s, %(nom_fecha_antiparasitario)s, %(mascota_id)s)"
        result = connectToMySQL('esquema_etologia').query_db(query, nuevo_form) #como respuesta me traerá el ID del registro que se acaba de crear 
        return result
        
    @classmethod
    def delete(cls,form):
        query = "DELETE FROM vacunas WHERE mascota_id = %(id)s"
        result = connectToMySQL('esquema_etologia').query_db(query, form)
        return result    