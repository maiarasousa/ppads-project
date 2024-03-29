from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from controller.turma_controller import TurmaController
from models import db

app = Flask(__name__)
# applies CORS headers to all routes, enabling resources to be accessed
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mssql+pyodbc://{usuario}:{senha}@{servidor}/{database}?driver=SQL+Server'.format(
        usuario = 'sa',
        senha = 'aplicando#2024guktdhg',
        servidor = 'localhost',
        database = 'SystemPresence'
    )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

db.init_app(app)

api = Api(app)

# use api.add_resource to add the paths
api.add_resource(TurmaController, '/turmas')

if __name__ == '__main__':
    app.run(port=5555, debug=True)