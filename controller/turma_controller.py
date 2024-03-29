from flask_restful import Resource

from models.model import Turma


class TurmaController(Resource):

    def get(self):
        turmas = Turma.query.all()
        return {'turmas': [turma.to_dict() for turma in turmas]}, 200
