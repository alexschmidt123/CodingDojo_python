from flask import Flask, render_template,redirect, request
from users import User
app = Flask(__name__)

@app.route('/')
def index():
    return redirect ('/users')

@app.route('/users')
def users():
    users = User.get_all_users()
    return render_template('index.html', users = users)

@app.route('/users/<int:user_id>')
def users_user_id(user_id):
    data = {
        'server_user_id': user_id
    }
    user = User.get_one_user(data)
    return render_template('show.html', user = user)

@app.route('/users/new')
def users_new():
    return render_template ('users_new.html')

@app.route('/users/insert', methods = ['POST'])
def users_insert():
    data = {
        'server_first_name': request.form['template_first_name'],
        'server_last_name': request.form['template_last_name'],
        'server_email': request.form['template_email']
    }
    User.save(data)
    return redirect ('/users')

@app.route('/users/<int:user_id>/edit')
def users_users_id_edit(user_id):
    data = {
        'server_user_id': user_id
    }
    user = User.get_one_user(data)
    return render_template('edit.html', user = user)

@app.route('/users/<int:user_id>/update', methods = ['POST'])
def user_user_id_update(user_id):
    data = {
        'user_id': user_id,
        # questions: why not server_user_id?
        'server_first_name': request.form['template_first_name'],
        'server_last_name': request.form['template_last_name'],
        'server_email': request.form['template_email']
    }
    User.update_user(data)
    return redirect (f'/users/{user_id}')

@app.route('/users/<int:user_id>/delete')
def users_users_id_delete(user_id):
    data ={
        'user_id' : user_id
    }
    User.delete(data)
    return redirect ('/users')


if __name__ == '__main__':
    app.run(debug = True) 