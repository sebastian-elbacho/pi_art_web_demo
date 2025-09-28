from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/fireshow')
def fireshow():
    return render_template('fireshow.html')

@app.route('/lightshow')
def lightshow():
    return render_template('lightshow.html')

@app.route('/lasershow')
def lasershow():
    return render_template('lasershow.html')

@app.route('/ilusionist')
def ilusionist():
    return render_template('ilusionist.html')

@app.route('/aerial')
def aerial():
    return render_template('aerial.html')








if __name__ == "__main__":
    app.run(debug=True)