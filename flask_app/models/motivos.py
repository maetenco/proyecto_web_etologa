from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
from .mascotas import Mascota

class Motivo:
    def __init__(self, data):
        self.motivo_consulta = data['motivo_consulta']
        self.otra_mascota = data['otra_mascota']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.mascota_id = data['mascota_id']

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
    def save(cls, form,mascota):

        nuevo_form= {'motivo_consulta': form['motivo_consulta'],
                    'otra_mascota': form['otra_mascota'], 
                    'momento_salida_a_calle': form['momento_salida_a_calle'], 
                    'mascota_id': mascota,
                    }
        
        query = "INSERT INTO motivos (motivo_consulta, otra_mascota, mascota_id) VALUES (%(motivo_consulta)s, %(otra_mascota)s, %(mascota_id)s)"
        result = connectToMySQL('esquema_etologia').query_db(query, nuevo_form) #como respuesta me traerá el ID del registro que se acaba de crear 
        return result
        
    @classmethod
    def update(cls, form):
        query = "UPDATE motivos SET motivo_consulta=%(motivo_consulta)s, otra_mascota=%(otra_mascota)s WHERE mascota_id=%(mascota_id)s" 
        result = connectToMySQL('esquema_etologia').query_db(query, form)
        return result
    
    @classmethod
    def delete(cls,form):
        query = "DELETE FROM motivos WHERE mascota_id = %(id)s"
        result = connectToMySQL('esquema_etologia').query_db(query, form)
        return result    