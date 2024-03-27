class AlunoRepository:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def obter_alunos(self):
        return self.alunos

    def atualizar_presenca(self, nome_aluno, presente):
        for aluno in self.alunos:
            if aluno['nome'] == nome_aluno:
                aluno['presente'] = presente
                return True
        return False

# Inicialização dos alunos
alunos_repo = AlunoRepository()
alunos_repo.adicionar_aluno({"nome": "Joao", "presente": False})
alunos_repo.adicionar_aluno({"nome": "Maria", "presente": False})
alunos_repo.adicionar_aluno({"nome": "Pedro", "presente": False})