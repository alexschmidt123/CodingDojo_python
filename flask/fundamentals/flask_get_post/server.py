from urllib import request
from flask import Flask, render_template, redirect,request
app = Flask(__name__)
@app.route('/') 
def index():
    return render_template ('index.html') 
@app.route('/handle_form', methods=['POST'])
def handle_form():
    print(request.form['f_name'])
    print(request.form['m_name'])
    return redirect ('result.html',
full_name = request.form['f_name'],mothers_maiden_name = request.form['m_name'],ssn = request.form['ssn'])
if __name__=="__main__":   
    app.run(debug=True)  

