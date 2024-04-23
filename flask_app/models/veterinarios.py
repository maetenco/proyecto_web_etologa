
from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #Patrón de email

class Veterinario:
    def __init__(self, data):
        #data = {diccionario con toda la info que quiero para mi instancia}
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


#Ahora debo validar al usuario, entonces creo otro método para validar, éste debe ser estático
    @staticmethod
    def validate_veterinario(form): #el mismo formulario anterior quiero que lo valide
        #form = {"firt_name":"Elena","last_name":"De Troya", "email":"elena@codingdojo.com", "password": LA QUIERO RECIBIR YA ENCRIPTADA}
        is_valid = True
        
        if len(form['first_name']) < 2: #valido el nombre primero y este debe tener al menos 2 caracteres
            flash('El nombre debe tener al menos 3 caracteres', "register_vet") #de la categoría de register (registro)
            is_valid = False
        
        if len(form['last_name']) < 2: #valido el apellido primero y este debe tener al menos 2 caracteres
            flash('El apellido debe tener al menos 3 caracteres', "register_vet") #de la categoría de register (registro)
            is_valid = False
        
        #verifico que el correo tenga el patrón correcto
        if not EMAIL_REGEX.match(form['email']):
            flash("E-mail inválido", "register_vet")
            is_valid = False

        #Valido que el correo sea único
        query = "SELECT * FROM veterinarios WHERE email = %(email)s"
        results = connectToMySQL('esquema_etologia').query_db(query, form)
        if len(results) >= 1:
            flash("E-mail registrado previamente", "register_vet")
            is_valid = False
        
        #validar que la contraseña tenga al menos 6 caracteres
        if len(form["password"]) < 6:
            flash("Tu contraseña debe tener al menos 6 caracteres", "register_vet")
            is_valid = False
        
        #valido que la contraseña y la confirmación de esta sean iguales
        if form["password"] != form["confirm"]:
            flash("Las contraseñas no coinciden", "register_vet")
            is_valid = False
        
        return is_valid
    
    @classmethod
    def save(cls, form):
        #form = {"firt_name":"Elena","last_name":"De Troya", "email":"elena@codingdojo.com", "password": LA QUIERO RECIBIR YA ENCRIPTADA}
        query = "INSERT INTO veterinarios (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        result = connectToMySQL('esquema_etologia').query_db(query, form) #como respuesta me traerá el ID del registro que se acaba de crear 
        return result

    @classmethod
    def get_by_id_vet(cls, form):
        #form = {"id": 1}
        query = "SELECT * FROM veterinarios WHERE id = %(id)s"
        result = connectToMySQL('esquema_etologia').query_db(query, form)
        #Esto me regresa una lista de diccionarios que sólo tiene una posición
        veterinario = cls(result[0])
        return veterinario
    


    @classmethod
    def get_by_email(cls, form): #recibo el formulario que será un diccionario que tiene el email que busco que también incluye el password ---->  form = {"email": "elena@codingdojo.com", "password": "Elenita"}
        query = "SELECT * FROM veterinarios WHERE email = %(email)s"
        results = connectToMySQL('esquema_etologia').query_db(query, form)
        if len(results) == 1:
            #si existe el usuario, me regresa sólo UN registro y tiene la posición cero [0]
            veterinario = cls(results[0])
            return veterinario #Entonces regreso la instancia del usuario con ese correo
        else:
            return False
"""





    #FLUJO: seleccionamos todas las columnas de la tabla de users donde el email sea el mismo que el usuario ingresó en el formulario.
    #Preguntamos si el tamaño de mi resultado es igual a 1, pues entonces si existe el usuario y creo una instancia con el diccionario que tengo en results
    #Y si no regresa False
    


"""