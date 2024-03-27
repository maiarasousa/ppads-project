class ChamadaController:
    def __init__(self, aluno_repository):
        self.aluno_repository = aluno_repository

    def realizar_chamada(self, turma, horario):
        alunos = self.aluno_repository.obter_alunos()

        chamada_info = {"turma": turma, "horario": horario, "alunos": []}
        
        for aluno in alunos:
            presenca = input(f"{aluno['nome']}: presente (S/N)? ").upper()
            aluno['presente'] = True if presenca == 'S' else False
            chamada_info["alunos"].append(aluno)
            self.aluno_repository.atualizar_presenca(aluno['nome'], aluno['presente'])
        
        return {"message": "Chamada realizada com sucesso", "chamada_info": chamada_info}