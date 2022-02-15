from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form['raspberry'])
    now = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    count = int(request.form['raspberry'])+ int(request.form['blackberry'])+int(request.form['strawberry'])+int(request.form['apple'])
    return render_template ('checkout.html',
apple = request.form['apple'],blackberry = request.form['blackberry'],strawberry = request.form['strawberry'],raspberry = request.form['raspberry'],firstName = request.form['first_name'],lastName = request.form['last_name'],email = request.form['email_a'], count = count, now = now)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)  