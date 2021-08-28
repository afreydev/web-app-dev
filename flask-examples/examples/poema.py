from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "This is the index!"

@app.route("/poema/<nombre>/escritor/<escritor>")
def poema(nombre, escritor):
    return render_template("poema.html", nombre=nombre, escritor=escritor)
