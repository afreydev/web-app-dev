from flask import Flask
app = Flask(__name__)

@app.route("/saludo/<nombre>")
def saludar(nombre):
    # muestra un saludo al usuario
    return "Hola {}, ¿cómo estás?".format(nombre)

@app.route("/calculadora/suma/<int:a>/mas/<int:b>")
def calcular(a, b):
    suma = a + b
    # muestra la suma de los valores ingresados
    return "{} + {}  = {}".format(a, b, suma)

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    # muestra el subpath después de /path/
    return "Subpath %s" % subpath

