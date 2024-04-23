#importaciones
from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app

#importacion de todos los modelos
from flask_app.models.veterinarios import Veterinario
from flask_app.models.mascotas import Mascota
from flask_app.models.tutores import Tutor
from flask_app.models.pre_consultas import Pre_consulta

#Importo bcrypt que es el que me escripta las contraseñas
from flask_bcrypt import Bcrypt

#ahora lo inicializo
bcrypt = Bcrypt(app)



"""


@app.route('/new')
def new_recipe():
    #verificar que el usuario inició sesión
    if 'user_id' not in session:
        return redirect('/')
    
    return render_template("new.html")

@app.route('/create', methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/')

    #validar que la info de recetas es correcta y luego PUEDO GUARDAR LA RECETA
    if not Recipe.validate_recipe(request.form):
        return redirect("/new")

    #guardo la receta y redirecciono a /recipes
    Recipe.save(request.form)
    #redireccionar a recipes
    return redirect ("/recipes")


@app.route("/edit/<int:id>")
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect("/")
    
    #id de la receta ---> para cerar una instancia de receta
    data_receta = {"id": id}
    #instancia de receta
    recipe = Recipe.get_by_id(data_receta)

    return render_template("edit.html", recipe=recipe)

@app.route('/update', methods=['POST'])
def update_recipe():
    if 'user_id' not in session:
        return redirect('/')
    
    #Recibo un request.form = {}  --> y quiero validar que la info sea correcta y luego PUEDO GUARDAR LA RECETA pero antes 
    #debo sacar el id desde request.form para poder decirle cuál es la receta que estoy modificando
    if not Recipe.validate_recipe(request.form):
        return redirect("/edit"+request.form['id'])
    
    #Si todo lo anterior está bien entonces que actualice y redirija a ("/recipes")
    Recipe.update(request.form)
    return redirect("/recipes")
    
@app.route("/delete/<int:id>")
def delete_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    
    data_receta = {"id": id}
    #necestio un método que me elimine la receta
    Recipe.delete(data_receta)
    return redirect('/recipes')


#de aquí para arriba

@app.route("/show/<int:id>")
def show_receta(id):
    if 'user_id' not in session:
        return redirect('/')
    
    info_receta = {"id": id}
    recipe = Recipe.show_recipe(info_receta)
    return render_template('show.html', recipe=recipe)

"""