from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
from .mascotas import Mascota

class Pre_consulta:
    def __init__(self, data):


        self.alimentacion_marca = data['alimentacion_marca']
        self.otro_animal = data['otro_animal']
        self.motivo_consulta = data['motivo_consulta']
        self.entrenamiento = data['entrenamiento']
        self.motivo_entrenamiento = data['motivo_entrenamiento']
        self.usa_farmacos = data['usa_farmacos']
        self.ayuda_farmacos = data['ayuda_farmacos']
        self.tipo_sujecion = data['tipo_sujecion']
        self.fecha_ultima_vac_octuple_sect_triple = data['fecha_ultima_vac_octuple_sect_triple']
        self.fecha_antiparasitario = data['fecha_antiparasitario']
        self.diagn_problem_fisico = data['diagn_problem_fisico']
        self.esta_en_tto = data['esta_en_tto']
        self.diagnostico = data['diagnostico']
        self.medicamentos = data['medicamentos']
        self.cuales_medicamentos = data['cuales_medicamentos']
        self.vomitos_diarrea = data['vomitos_diarrea']
        self.examenes = data['examenes']

        self.mascota_id = data['mascota_id']
        self.mascota_nombre = data['mascota_nombre']
        self.tutor_id = data['tutor_id']
        self.tutor_nombre_apellido = data['nombre']+['apellido']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



"""
from flask_app.config.mysqlconnection import connectToMySQL
#importo flash para mostrar mensajes temporales, los que me sirven para mostrar errores en la la validación
from flask import flash
#from .users import User

class Recipe:
    def __init__(self, data):
        #data = {diccionario con toda la info que quiero para mi instancia}
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        self.user_name = data['user_name']

    #método que me valide la información del formulario al ingresar la receta
    @staticmethod
    def validate_recipe(form):
        #Aquí recibe el request.form
        is_valid = True

        if len(form['name']) < 3:
            is_valid = False
            flash("El nombre de la receta debe tener al menos 3 caracteres", "receta")

        if len(form['description']) < 3:
            is_valid = False
            flash("La descripción de la receta debe tener al menos 3 caracteres", "receta")

        if len(form['instructions']) < 3:
            is_valid = False
            flash("Las instrucciones de la receta debe tener al menos 3 caracteres", "receta")

        if form["date_made"] == "":
            is_valid = False
            flash("Ingresa una fecha de creación", "receta")
        
        return is_valid


    @classmethod
    def save(cls, form):
        query = "INSERT INTO recipes (name, description, instructions, date_made, under_30, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s,%(under_30)s, %(user_id)s)"
        result = connectToMySQL('esquema_recetas').query_db(query, form) #como respuesta me traerá el ID del registro que se acaba de crear 
        return result
        
    @classmethod
    def get_all(cls):
        query = "SELECT recipes.*, users.first_name AS user_name FROM recipes JOIN users ON recipes.user_id = users.id"
        results = connectToMySQL('esquema_recetas').query_db(query)
        recipes = []
        for recipe in results:
            #recipe = {diccionario que recibo de BD - registro con columnas}
            recipes.append(cls(recipe)) #cls(recipe) --> genera ula instancia en base al diccionario y el recipes.append agrega esa instancia a la lista de recetas
        return recipes
    
    @classmethod
    def get_by_id(cls, data):
        #data = {"id": 2}
        query = "SELECT recipes.*, users.first_name as user_name FROM recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s"
        result = connectToMySQL('esquema_recetas').query_db(query, data) #recibo una lista con un diccionario
        recipe = cls(result[0])
        return recipe
    
    @classmethod
    def update(cls, form):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under_30 = %(under_30)s WHERE id = %(id)s"
        result = connectToMySQL('esquema_recetas').query_db(query, form)
        return result
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL('esquema_recetas').query_db(query, data)


    #de aquí para abajo
    @classmethod
    def show_recipe(cls, data):
        query = "SELECT recipes.*, users.first_name as user_name FROM recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s"
        result = connectToMySQL('esquema_recetas').query_db(query, data)
        return result 


"""