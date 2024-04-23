#pipenv install flask pymysql  flask-bcrypt
#importo app
from flask_app import app


#importacion de controladores ---> pendientei. Importar controlador recetas
from flask_app.controllers import mascotas_controller, veterinarios_controller, tutores_controller, pre_consultas_controller, web_controller


if __name__ == "__main__":
    app.run(debug=True) #(debug=True, port=3400) 
    #lo anterior si quisiera poner otro puerto o modificar mi servidor local

