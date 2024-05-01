from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Mascota:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.tutor_id = data['tutor_id']
        self.veterinario_id = data['veterinario_id']



    @classmethod
    def get_all_mascotas(cls):
        query = "SELECT mascotas.id, mascotas.nombre AS nombre_mascota, mascotas.tutor_id, tutores.nombre AS nombre_tutor, tutores.apellido AS apellido_tutor, tutores.id FROM mascotas JOIN tutores ON tutor_id = tutores.id;"
        results = connectToMySQL('esquema_etologia').query_db(query)
        mascotas = []
        for mascota in results:
            #recipe = {diccionario que recibo de BD - registro con columnas}
            mascotas.append(cls(mascota)) #cls(recipe) --> genera ula instancia en base al diccionario y el recipes.append agrega esa instancia a la lista de recetas
        return mascotas
    
    #debo crear mascotas
    
    @classmethod
    def save(cls, form):
        query = "INSERT INTO mascotas (nombre, tutor_id, veterinario_id) VALUES (%(nombre)s, %(tutor_id)s, %(veterinario_id)s)"
        result = connectToMySQL('esquema_etologia').query_db(query, form) #como respuesta me traerá el ID del registro que se acaba de crear 
        return result