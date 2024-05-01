from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
from .mascotas import Mascota

class Diagnostico_previo:
    def __init__(self, data):
        self.diagnostico = data['diagnostico']
        self.esta_en_tto = data['esta_en_tto']
        self.problema_fisico = data['problema_fisico']
        self.medicamentos = data['medicamentos']
        self.examenes = data['examen']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.mascota_id = data['mascota_id']

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

        if len(form['medicamentos']) < 3:
            is_valid = False
            flash("Si no toma medicamentos escriba 'No toma', de lo contrario agregue los medicamentos que su mascota toma", "form_diagnostico_previo")

        return is_valid
    
    @classmethod
    def save(cls, form,mascota):

        nuevo_form= {'diagnostico': form['diagnostico'],
                    'esta_en_tto': form['esta_en_tto'], 
                    'problema_fisico': form['problema_fisico'], 
                    'medicamentos': form['medicamentos'], 
                    'examen': form['examen'], 
                    'mascota_id': mascota,                     
                    }
        

        query = "INSERT INTO diagn_previo (diagnostico, esta_en_tto, problema_fisico, medicamentos, examenes,mascota_id) VALUES (%(diagnostico)s, %(esta_en_tto)s, %(problema_fisico)s, %(medicamentos)s, %(examen)s,%(mascota_id)s)"
        result = connectToMySQL('esquema_etologia').query_db(query, nuevo_form) #como respuesta me traerá el ID del registro que se acaba de crear 
        return result
        
    @classmethod
    def delete(cls,form):
        query = "DELETE FROM diagn_previo WHERE mascota_id = %(id)s"
        result = connectToMySQL('esquema_etologia').query_db(query, form)
        return result    