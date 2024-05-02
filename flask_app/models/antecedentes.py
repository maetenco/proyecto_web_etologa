from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
from .mascotas import Mascota
from .tutores import Tutor


class Antecedente:
    def __init__(self, data):
        self.id = data['id']
        self.nombre_mas = data['nombre_mas']
        self.dog_or_cat = data['dog_or_cat']
        self.raza = data['raza']
        self.fecha_nac = data['fecha_nac']
        self.edad = data['edad']
        self.peso = data['peso']
        self.sexo = data['sexo']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.mascota_id = data['mascota_id']

    @classmethod
    def save(cls,form,mascota):

        nuevo_form= {'nombre_mas': form['nombre_mas'],
                    'dog_or_cat': form['dog_or_cat'], 
                    'raza': form['raza'], 
                    'fecha_nac': form['fecha_nac'], 
                    'edad': form['edad'], 
                    'peso': form['peso'], 
                    'sexo': form['sexo'], 
                    'mascota_id': mascota,                     
                    }

        query = "INSERT INTO antecedentes (nombre_mas, dog_or_cat, raza, fecha_nac, edad, peso, sexo,mascota_id) VALUES (%(nombre_mas)s, %(dog_or_cat)s, %(raza)s, %(fecha_nac)s,%(edad)s, %(peso)s, %(sexo)s,%(mascota_id)s)"
        result = connectToMySQL('esquema_etologia').query_db(query, nuevo_form) #como respuesta me traerá el ID del registro que se acaba de crear 
        return result
    
    @staticmethod
    def get_mascota(form):
        query = "SELECT antecedentes.mascota_id AS id, antecedentes.nombre_mas AS nombre_mas, antecedentes.dog_or_cat as dog_or_cat FROM antecedentes JOIN mascotas ON antecedentes.mascota_id = mascotas.id WHERE mascotas.tutor_id = %(id)s"
        results = connectToMySQL('esquema_etologia').query_db(query,form)
        mascota = []
        for m in results:
            mascota.append(m)        
        return mascota
    
    @staticmethod
    def obtener_mascota(form):
        query = "SELECT antecedentes.mascota_id, UPPER(antecedentes.nombre_mas) AS nombre, dog_or_cat, raza, fecha_nac, edad, peso, sexo, mascotas.tutor_id FROM antecedentes JOIN mascotas ON antecedentes.mascota_id = mascotas.id JOIN tutores ON mascotas.tutor_id = tutores.id WHERE mascotas.id = %(id)s"
        results = connectToMySQL('esquema_etologia').query_db(query,form)
        mascota = []
        for m in results:
            mascota.append(m)        
        return mascota
    
    @classmethod
    def delete(cls,form):
        query = "DELETE FROM antecedentes WHERE mascota_id = %(id)s"
        result = connectToMySQL('esquema_etologia').query_db(query, form)
        return result    