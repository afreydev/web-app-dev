from flask import Flask
app = Flask(__name__)

@app.route("/slash")
def sin_slash():
    # muestra un saludo al usuario
    return "Sin slash"

@app.route("/slash/")
def con_slash():
    return "Con slash"
