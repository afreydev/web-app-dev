from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/formulario", methods=['POST','GET'])
def formulario():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']
    
    return "Tu nombre es: {} - Apellido: {} - Edad: {}".format(nombre, apellido, edad)

@app.route("/formulariovalidado", methods=['POST'])
def formulario_validado():
    nombre = request.form.get('nombre', 'Nombre genérico')
    apellido = request.form.get('apellido', 'Apellido inventado')
    edad = request.form.get('edad','45')

    return "Tu nombre es: {} - Apellido: {} - Edad: {}".format(nombre, apellido,edad)

@app.route("/enlaurl", methods=['GET'])
def enlaurl():
    token = request.args.get('secret')
    return "Esta es una clave ultra secreta: {}".format(token)

@app.route("/esjson", methods=['POST'])
def esjson():
    data = request.get_json()
    nombre = data['nombre']
    apellido = data['apellido']
    edad = data['edad']
    
    return "Tu nombre es: {} - Apellido: {} - Edad: {}".format(nombre, apellido,edad)

@app.route("/retornajson", methods=['GET'])
def retornajson():
    pelicula = {
            "nombre": "The terminator",
            "año": 1986,
            "director": "James Cameron"
            }
    return jsonify(pelicula)

