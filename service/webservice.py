from flask import Flask, jsonify, request
from controller.chamada_controller import ChamadaController
from repository.aluno_repository import AlunoRepository

app = Flask(_name_)
aluno_repository = AlunoRepository()
controller = ChamadaController(aluno_repository)

@app.route('/realizar_chamada', methods=['POST'])
def realizar_chamada():
    data = request.json
    turma = data['turma']
    horario = data['horario']
    result = controller.realizar_chamada(turma, horario)
    return jsonify(result)

if _name_ == 'main':
    app.run(debug=True)
