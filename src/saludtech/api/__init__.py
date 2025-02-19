import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_swagger import swagger
from dotenv import load_dotenv

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def importar_modelos_alchemy():
    pass

def create_app(configuracion=None):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    # Configuracion de BD
    app.config['SQLALCHEMY_DATABASE_URI'] =  os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

     # Inicializa la DB
    from saludtech.config.db import init_db
    init_db(app)

    from saludtech.config.db import db

    importar_modelos_alchemy()

    with app.app_context():
        db.create_all()

     # Importa Blueprints

    # Registro de Blueprints

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
