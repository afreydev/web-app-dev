from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "This is the index!"

@app.route("/ejemplo-template")
def ejemploTemplate():
    nombre = "Lucas Albeiro"
    bandera = True
    peliculas = ["Titanic","Terminator","La historia sin fin"];
    return render_template("template-ej.html", peliculas=peliculas, nombre=nombre, bandera=bandera)
