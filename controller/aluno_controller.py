from flask_restful import Resource

from models.model import Aluno


class AlunoController(Resource):

    def get(self):
        alunos = Aluno.query.all()
        return {'alunos': [aluno.to_dict() for aluno in alunos]}, 200
