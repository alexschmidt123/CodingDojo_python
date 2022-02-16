from flask import Flask, render_template,session,redirect, request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
@app.route('/')
def index():
    # if 'count' not in session:
    #     session['count']=0
    session['count']+=1
    return render_template('index.html', count = session['count'])


@app.route('/destroy_session')
def refresh():
    # if 'count' in session:
    session['count'] = 0
    return  redirect ('/')


@app.route('/addtwo')
def addtwo():
    session['count']+=1
    return redirect('/')
@app.route('/reset')
def reset():
    session['count']=0
    return redirect('/')

# first I used global count. 
# @app.route('/', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     # Here we add two properties to session to store the name and email
#     session['username'] = request.form['name']
#     session['useremail'] = request.form['email']
#     return redirect('/show')

# @app.route('/show')
# def show_user():
#     return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])



if __name__ == "__main__":
    app.run(debug=True)

