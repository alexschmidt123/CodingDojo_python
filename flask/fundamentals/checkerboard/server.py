from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/4')
def index1():
    return render_template('index1.html')

@app.route('/<int:x>/<int:y>')
def index2(x,y):
    return render_template('index2.html', x = x, y =y)

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def index3(x,y,color1,color2):
    return render_template('index3.html', x = x, y =y, color1 = color1,color2=color2)


if __name__=="__main__": 
    app.run(debug=True)   
