from re import M
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.meal import Meal
from flask import flash

@app.route('/dashboard')
def success():
    # session['user_id']==None
    if 'user_id' not in session:
        flash("Please log in to view this resource")
        return redirect('/')
    meals = Meal.get_all_meals()
    return render_template('dashboard.html', meals = meals)

@app.route('/recipes/<int:meal_id>')
def meals_meal_id(meal_id):
    data = {
        'server_meal_id': meal_id
    }
    meal = Meal.get_one_meal(data)
    return render_template('view.html', meal = meal)


@app.route('/recipes/new')
def meals_new():
    return render_template ('new.html')


@app.route('/recipes/new/create', methods = ['POST'])
def meals_insert():
    print (request.form)
    if not Meal.validate_new_meal(request.form):
        print("validation fails")
        return redirect('/recipes/new')
    else:
        data = {
            "server_user_id": session['user_id'],
            'server_name': request.form['template_name'],
            'server_description': request.form['template_description'],
            'server_instruction': request.form['template_instruction'],
            'server_under_30_minute': request.form['template_under_30_minute'],
            'server_made_date': request.form['template_made_date']
        }
        Meal.save(data)
        return redirect ('/dashboard')

@app.route('/recipes/edit/<int:meal_id>')
def meals_meal_id_edit(meal_id):
    data = {
        'server_meal_id': meal_id
    }
    meal = Meal.get_one_meal(data)

    return render_template('edit.html', meal = meal)

@app.route('/recipes/edit/update/<int:meal_id>', methods = ['POST', 'GET'])
def meals_meal_id_update(meal_id):
    data = {
        "meal_id": meal_id,
        'server_name': request.form['template_name'],
        'server_description': request.form['template_description'],
        'server_instruction': request.form['template_instruction'],
        'server_under_30_minute': request.form['template_under_30_minute'],
        'server_made_date': request.form['template_made_date']
    }
    print(data)
    Meal.update_meal(data)
    return redirect ('/dashboard')

@app.route('/recipes/delete/<int:meal_id>')
def meals_meal_id_delete(meal_id):
    data ={
        'meal_id' : meal_id
    }
    Meal.delete(data)
    return redirect ('/dashboard')