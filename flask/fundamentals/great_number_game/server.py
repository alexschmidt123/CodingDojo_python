from flask import Flask, render_template, redirect, request, session  # Import Flask to allow us to create our app
import random
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secrect_key = '12l3'

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    session['computer_num'] = random.randint(1,100)
    return render_template('index.html')

@app.route('/process_guess')
def process_guess():
    print('***************************************')
    print("request.form dictionary:{request.form}")
    print(f"User guessed: {request.form['guess']}")
    print(f"Computer Number: {session['computer_num']}")
    user_guess =int(request.form["guess"])
    computer_num = int(session['computer_num'])
    if (user_guess>computer_num):
        is_too_high= True
        print('GUESSED TOO HIGH')
    elif(user_guess<computer_num):
        is_too_low = True
        print('GUESSED TOO LOW')
    else:
        is_correct = True
        print('GUESSED CORRECT')
    return redirect ('/results')
    


@app.route('/result')
def result():
    #check the booleans
    return render_template('result.html')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

