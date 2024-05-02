from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
from .mascotas import Mascota
from .tutores import Tutor


class Examen:
    def __init__(self, data):
        self.id = data['id']
        self.examen = data['examen']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.mascota_id = data['mascota_id']

    @classmethod
    def save(cls, form,mascota):

        nuevo_form= {'examen': form,
                    'mascota_id': mascota,
                    }
        
        query = "INSERT INTO examenes (examen,mascota_id) VALUES (%(examen)s,%(mascota_id)s)"
        result = connectToMySQL('esquema_etologia').query_db(query, nuevo_form) #como respuesta me traerá el ID del registro que se acaba de crear 
        return result
    
    @classmethod
    def update(cls, form):
        query = "UPDATE examenes SET examen=%(examen)s WHERE mascota_id=%(mascota_id)s" 
        result = connectToMySQL('esquema_etologia').query_db(query, form)
        return result
    
    @classmethod
    def delete(cls,form):
        query = "DELETE FROM examenes WHERE mascota_id = %(id)s"
        result = connectToMySQL('esquema_etologia').query_db(query, form)
        return result   