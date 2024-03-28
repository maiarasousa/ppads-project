from flask import Flask, jsonify, request
from controller.chamada_controller import ChamadaController

app = Flask(__name__)
controller = ChamadaController()

@app.route('/realizar_chamada', methods=['POST'])
def realizar_chamada():
    data = request.json
    turma = data['turma']
    horario = data['horario']
    result = controller.realizar_chamada(turma, horario)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
