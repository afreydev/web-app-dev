from flask import Flask, url_for

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

with app.test_request_context():
    print(url_for('saludar', nombre="Pedrito"))
    print(url_for('calcular', a=3, b=10))
    print(url_for('show_subpath', subpath='/rutica/'))
