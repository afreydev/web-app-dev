from flask import Flask
app = Flask(__name__)

@app.route("/")
def imagen():
    # muestra un saludo al usuario
    return "Esta es la prueba de imagenes"
