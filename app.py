from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
 



@app.route('/fire')
def fireshow():
    return render_template('fire.html')

@app.route('/lightshow')
def lightshow():
    return render_template('light.html')

@app.route('/lasershow')
def lasershow():
    return render_template('laser.html')

@app.route('/ilusionist')
def ilusionist():
    return render_template('ilusionist.html')

@app.route('/aerial')
def aerial():
    return render_template('aerial.html')


@app.route('/inne') 
def inne():
    return render_template('inne.html')







if __name__ == "__main__":
    app.run(debug=True)