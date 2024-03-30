from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from controller.aluno_controller import AlunoController
from controller.turma_controller import TurmaController
from controller.chamada_controller import ChamadaController

from models import db

app = Flask(__name__)
# applies CORS headers to all routes, enabling resources to be accessed
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mssql+pyodbc://{usuario}:{senha}@{servidor}/{database}?driver={driver}'.format(
        usuario='sa',
        senha='aplicando#2024guktdhg',
        servidor='host.docker.internal',
        # servidor='localhost',
        database='SystemPresence',
        driver='ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes'
        # driver='SQL+Server'
    )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

db.init_app(app)

api = Api(app)

# use api.add_resource to add the paths
api.add_resource(TurmaController, '/turmas')
api.add_resource(AlunoController, '/alunos')
api.add_resource(ChamadaController, '/alunos/<int:aluno_id>/frequencia')

if __name__ == '__main__':
    app.run(port=5000, debug=False)
