from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
from .mascotas import Mascota

class Diagnostico_previo:
    def __init__(self, data):
        self.diagnostico = data['diagnostico']
        self.esta_en_tto = data['esta_en_tto']
        self.problema_fisico = data['problema_fisico']
        self.medicamentos = data['medicamentos']
        self.examenes = data['examenes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_diagnostico_previo(form):
        #Aquí recibe el request.form
        is_valid = True

        if len(form['diagnostico']) < 3:
            is_valid = False
            flash("Si no tiene diagnósticos previos escriba 'No tiene', de lo contrario incluya el diagnóstico que tiene su mascota", "form_diagnostico_previo")

        if len(form['problema_fisico']) < 3:
            is_valid = False
            flash("Si no tiene problemas físicos escriba 'No tiene', de lo contrario explique el problema físico que tiene su mascota", "form_diagnostico_previo")

        if len(form['cuales_medicamentos']) < 3:
            is_valid = False
            flash("Si no toma medicamentos escriba 'No toma', de lo contrario agregue los medicamentos que su mascota toma", "form_diagnostico_previo")

        return is_valid
    
    @classmethod
    def save(cls, form):
        query = "INSERT INTO diagnosticos_previos (diagnostico, esta_en_tto, problema_fisico, medicamentos, cuales_medicamentos, examenes) VALUES (%(diagnostico)s, %(esta_en_tto)s, %(problema_fisico)s, %(medicamentos)s,%(cuales_medicamentos)s, %(examenes)s)"
        result = connectToMySQL('esquema_etologia').query_db(query, form) #como respuesta me traerá el ID del registro que se acaba de crear 
        return result
        