import os
from uuid import UUID
from flask import Flask, jsonify
from anonimizador.api.anonimizador import bp as anonimizador_bp
from anonimizador.config.db import init_db
from anonimizador.modulos.anonimizador.infraestructura.modelos import importar_modelos_alchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Monoliticas2025#@34.60.201.230:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

basedir = os.path.abspath(os.path.dirname(__file__))

init_db(app)
importar_modelos_alchemy()

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Hello, World!"})

app.register_blueprint(anonimizador_bp, url_prefix="/api/anonimizador")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=0, debug=True)