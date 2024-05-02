from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
from .mascotas import Mascota
from .tutores import Tutor


class Derivacion:
    def __init__(self, data):
        self.id = data['id']
        self.derivaciones = data['derivaciones']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.mascota_id = data['mascota_id']

    @classmethod
    def save(cls, form,mascota):

        nuevo_form= {'derivaciones': form,
                    'mascota_id': mascota,
                    }
        
        query = "INSERT INTO derivaciones (derivacion,mascota_id) VALUES (%(derivaciones)s,%(mascota_id)s)"
        result = connectToMySQL('esquema_etologia').query_db(query, nuevo_form) #como respuesta me traerá el ID del registro que se acaba de crear 
        return result

    @classmethod
    def update(cls, form):
<<<<<<< HEAD
        query = "UPDATE derivaciones SET derivacion=%(derivacion)s WHERE mascota_id=%(mascota_id)s" 
=======
        query = "UPDATE derivaciones SET derivacion=%(derivaciones)s WHERE mascota_id=%(mascota_id)s" 
>>>>>>> 71a16bd37b64eb59cae8fa5eecacb55f5b5eb1b7
        result = connectToMySQL('esquema_etologia').query_db(query, form)
        return result
    
    @classmethod
    def delete(cls,form):
        query = "DELETE FROM derivaciones WHERE mascota_id = %(id)s"
        result = connectToMySQL('esquema_etologia').query_db(query, form)
        return result   