import os
from flask import Flask, jsonify
from flask_swagger import swagger
from dotenv import load_dotenv

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def importar_modelos_alchemy():
    ##import saludtech.modulos.procesador_imagenes.infraestructura.dto
    import saludtech.modulos.procesador_imagenes.infraestructura.modelos


def create_app(configuracion=None):
    # Initialize the Flask application
    app = Flask(__name__, instance_relative_config=True)

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Monoliticas2025#@34.60.201.230:5432/postgres" #os.getenv("DATABASE_URL", "postgresql://postgres:Monoliticas2025#@34.60.201.230:5432/postgres")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the DB
    from saludtech.config.db import init_db
    init_db(app)

    from saludtech.config.db import db

    # Import ORM models
    importar_modelos_alchemy()

    with app.app_context():
        db.create_all()

    # Import Blueprints for the new routes
    from saludtech.api.procesador_imagenes import bp as procesador_imagenes_bp

    # Register the blueprint with a URL prefix
    app.register_blueprint(procesador_imagenes_bp, url_prefix="/api")

    # @app.route("/spec")
    # def spec():
    #     swag = swagger(app)
    #     swag['info']['version'] = "1.0"
    #     swag['info']['title'] = "My API"
    #     return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
