import random
from datetime import datetime

from flask import request
from flask_restful import Resource

from db import db
from models.model import Frequencia


class ChamadaController(Resource):

    def post(self, aluno_id):
        data = request.get_json()

        presente = data.get('presente')
        id = random.randint(1111, 9999)
        data_chamada = datetime.now()

        novoRegistro = Frequencia(IdFrequencia=id, DataChamada=data_chamada, Presente=presente)
        db.session.add(novoRegistro)
        db.session.commit()

        freq = Frequencia.query.get(id)

        return {'frequencia': freq.to_dict()}, 201
