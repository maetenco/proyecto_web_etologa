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
            mascotas.append(cls(mascota)) 
        return mascotas
    
    #debo crear mascotas
    
    @classmethod
    def save(cls, form):
        query = "INSERT INTO mascotas (nombre, tutor_id, veterinario_id) VALUES (%(nombre)s, %(tutor_id)s, %(veterinario_id)s)"
        result = connectToMySQL('esquema_etologia').query_db(query, form) #como respuesta me traerá el ID del registro que se acaba de crear 
        return result
    
    @staticmethod
    def ver_mascotas():
        query = "SELECT mascotas.id, mascotas.nombre AS nombre, mascotas.tutor_id AS tutor_id,  tutores.nombre AS nombre_tutor,  tutores.apellido AS apellido_tutor, antecedentes.dog_or_cat FROM mascotas JOIN tutores ON tutor_id = tutores.id JOIN antecedentes ON antecedentes.mascota_id = mascotas.id"
        results = connectToMySQL('esquema_etologia').query_db(query)
        mascotas = []
        for mascota in results:
            mascotas.append(mascota)
        return mascotas
    
    @staticmethod
    def obtener_mascota(dicc):
        query = "SELECT a.mascota_id, m.nombre, a.dog_or_cat, a.raza, a.fecha_nac, a.edad, a.peso, a.sexo, m.tutor_id, ad.edad_adopcion, ad.donde_adquisicion, ad.tiempo_con_madre_hrnos, ad.momento_salida_a_calle, v.nom_fecha_ultima_vac, v.nom_fecha_antiparasitario, c.castracion, c.motivo_castracion, c.fecha_castracion, alim.tipo_alimentacion, e.tuvo_entrenamiento,e.motivo_entrenamiento, dp.diagnostico, dp.esta_en_tto, dp.problema_fisico, dp.medicamentos, mot.motivo_consulta, mot.otra_mascota FROM antecedentes a JOIN mascotas m ON a.mascota_id = m.id JOIN tutores ON m.tutor_id = tutores.id JOIN adquisiciones ad ON m.id = ad.mascota_id JOIN vacunas v ON m.id = v.mascota_id JOIN castraciones c ON m.id = c.mascota_id JOIN alimentaciones alim ON m.id = alim.mascota_id JOIN entrenamientos e ON m.id = e.mascota_id JOIN diagn_previo dp ON m.id = dp.mascota_id JOIN motivos mot ON m.id = mot.mascota_id WHERE m.id = %(id)s"
        results = connectToMySQL('esquema_etologia').query_db(query,dicc)
        mascota = results[0]
        return mascota
    
    @staticmethod
    def obtener_todas_mascota(dicc):
        query = "SELECT a.mascota_id, UPPER(a.nombre_mas) AS nombre, a.dog_or_cat, a.raza, a.fecha_nac, a.edad, a.peso, a.sexo, m.tutor_id, ad.edad_adopcion, ad.donde_adquisicion, ad.tiempo_con_madre_hrnos, ad.momento_salida_a_calle, v.nom_fecha_ultima_vac, v.nom_fecha_antiparasitario, c.castracion, c.motivo_castracion, c.fecha_castracion, alim.tipo_alimentacion, e.tuvo_entrenamiento,e.motivo_entrenamiento, dp.diagnostico, dp.esta_en_tto, dp.problema_fisico, dp.medicamentos, mot.motivo_consulta, mot.otro_animal FROM antecedentes a JOIN mascotas m ON a.mascota_id = m.id JOIN tutores ON m.tutor_id = tutores.id JOIN adquisiciones ad ON m.id = ad.mascota_id JOIN vacunas v ON m.id = v.mascota_id JOIN castraciones c ON m.id = c.mascota_id JOIN alimentaciones alim ON m.id = alim.mascotas_id JOIN entrenamientos e ON m.id = e.mascota_id JOIN diagn_previo dp ON m.id = dp.mascota_id JOIN motivos mot ON m.id = mot.mascota_id"
        results = connectToMySQL('esquema_etologia').query_db(query,dicc)
        mascotas = []
        for mascota in results:
            mascotas.append(mascota)
        return mascotas
    
    @classmethod
    def update(cls, form):
        query = "UPDATE mascotas SET nombre=%(nombre)s WHERE id=%(mascota_id)s" 
        result = connectToMySQL('esquema_etologia').query_db(query, form)
        return result
    
    @classmethod
    def delete(cls,form):
        query = "DELETE FROM mascotas WHERE id = %(id)s"
        result = connectToMySQL('esquema_etologia').query_db(query, form)
        return result    
