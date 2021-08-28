from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "This is the index!"

@app.route("/hello")
@app.route("/hello/<nombre>")
def hello(nombre=None):
    return render_template("hello.html", nombre=nombre)
