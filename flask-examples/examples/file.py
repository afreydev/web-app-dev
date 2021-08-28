from flask import Flask, request
app = Flask(__name__)

@app.route("/file", methods=['POST'])
def file():
    f = request.files['archivo']
    f.save('./files/{}'.format(f.filename))
    return "File OK!"
