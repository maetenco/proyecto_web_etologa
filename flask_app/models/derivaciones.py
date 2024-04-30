from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
from .mascotas import Mascota
from .tutores import Tutor


class Derivacion:
    def __init__(self, data):
        self.id = data['id']
        self.derivacion = data['derivacion']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, form):
        query = "INSERT INTO derivaciones (examen) VALUES (%(derivacion)s)"
        result = connectToMySQL('esquema_etologia').query_db(query, form) #como respuesta me traerá el ID del registro que se acaba de crear 
        return result
    