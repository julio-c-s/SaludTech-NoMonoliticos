import os
from flask import Flask, jsonify
from flask_swagger import swagger
from dotenv import load_dotenv

def importar_modelos_alchemy():
    # Importa el modelo para que SQLAlchemy lo registre
    from saludtech.infrastructure.repository import ImageModel
    # Forzamos el acceso al atributo para que se registre en la metadata
    _ = ImageModel.__tablename__

def create_app(configuracion=None):
    app = Flask(__name__, instance_relative_config=True)
    load_dotenv()

    # Configuración de la BD
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if not app.config['SQLALCHEMY_DATABASE_URI']:
        raise RuntimeError('Error: DATABASE_URL no está definida en .env')

    # Inicializa la base de datos
    from saludtech.config.db import init_db, db
    init_db(app)

    importar_modelos_alchemy()

    with app.app_context():
        db.create_all()

    # Importa y registra el blueprint de imágenes
    from saludtech.api.image_blueprint import image_bp
    app.register_blueprint(image_bp, url_prefix='/api')

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
