from flask_app.config.mysqlconnection import connectToMySQL #Conexión con BD
from flask import flash #flash es el encargado de mandar mensajes/errores
from datetime import datetime #Manipular fechas y saber la fecha actual
from flask import jsonify
import json
import pymysql.cursors

class Agenda:

    def __init__(self, data):
        self.start = data['start']
        self.end = data['end']
        self.title = data['title']

    @classmethod
    def get_all(cls):
        query = "SELECT  REPLACE(CAST(start AS char),' ','T') as start, replace(CAST(end AS char),' ','T') as end, "
        query += "title "
        query +=" from agenda where month(start) = month(CURRENT_DATE()) and year(start) = year(CURRENT_DATE())"
        result_list = connectToMySQL('esquema_etologia').query_db(query)

        fetchedData = json.dumps(result_list)
    #    record = json.loads(fetchedData)
    #    print("Respuesta :")
    #    print(record)

        return fetchedData
#        return agendas

    @classmethod
    def delete(cls, form):
        #form = {"id": 1}
        query = "DELETE FROM citas WHERE id = %(id)s"
        result = connectToMySQL('esquema_estado_reviewer').query_db(query, form)
        return result