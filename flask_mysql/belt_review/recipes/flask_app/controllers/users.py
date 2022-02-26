from flask_app import app

from flask import render_template, redirect, request, session

from flask_app.models.user import User
from flask import flash

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)




@app.route('/')
def index():

    return render_template ('register_and_login.html')

@app.route ('/users/register', methods = ['POST'])
def register_user():

    if not User.validate_new_user(request.form):
        print("validation fails")
        return redirect('/')

    else:
        print("validation good")
        data = {
            'first_name': request.form ['first_name'],
            'last_name': request.form ['last_name'],
            'email': request.form ['email'],
            'password': bcrypt.generate_password_hash(request.form ['password'])
        }
        print(data)
        User.create_new_user(data)
        flash("User registered; log in with that account")
        return redirect('/')

@app.route ('/users/login', methods = ['POST'])
def login_user():

    user = User.get_user_by_email(request.form)
    print(f'user: {user}')
    if not user:
        flash("User with given email does not exist.")
        return redirect ('/') 
    print('past first if check')

    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash ("Password is incorrect.")
        return redirect ('/')
    print('past second if check')
    #session is template data base in browser
    session['user_id'] = user.id
    session['user_first_name'] = user.first_name
    print(f'session: {session}')
    print('past session assignment')

    return redirect('/dashboard')

@app.route('/dashboard')
def success():

    if not "user_id" in session:
        flash("Please log in to view this resource")
        return redirect('/')
    
    return render_template('dashboard.html')

@app.route('/users/logout')
def logout():
    session.clear()
    flash(" Logged out; please log in again")
    return redirect ('/')