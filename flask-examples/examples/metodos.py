from flask import Flask, request

app = Flask(__name__)

@app.route('/metodos', methods=['GET', 'POST'])
def metodos():
    if request.method == 'GET':
        return metodo_get()
    else:
        return metodo_post()

def metodo_get():
    return "Este es el GET"

def metodo_post():
    return "Este es el POST"
