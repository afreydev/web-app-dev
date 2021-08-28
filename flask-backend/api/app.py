from flask import Flask

def create_app(test_config=None):   
    app = Flask(__name__, instance_relative_config=True)

    from modules.companies import bp as bpcompanies
 
    app.register_blueprint(bpcompanies)

    return app
