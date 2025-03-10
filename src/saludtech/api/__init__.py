import os
from flask import Flask, jsonify
from saludtech.api.procesador import bp as anonimizador_bp
from saludtech.config.db import init_db
from saludtech.modulos.procesador.infraestructura.modelos import importar_modelos_alchemy
from saludtech.modulos.sagas.aplicacion.global_vars import saga_coordinator_global  # Importa la instancia global

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Monoliticas2025#@34.60.201.230:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)
importar_modelos_alchemy()

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Hello, World!"})

app.register_blueprint(anonimizador_bp, url_prefix="/api/anonimizador")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=0, debug=True)
