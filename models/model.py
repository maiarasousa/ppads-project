from db import db


class Turma(db.Model):
    __tablename__ = 'Turma'

    IdTurma = db.Column(db.Integer, primary_key=True)
    NomeTurma = db.Column(db.String(50), unique=False, nullable=False)
    AnoLetivo = db.Column(db.Integer, unique=False, nullable=False)

    alunos = db.relationship('Aluno', secondary='Aluno_Turma', back_populates='turmas', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.IdTurma,
            'nome': self.NomeTurma,
            'ano_letivo': self.AnoLetivo,
            # 'alunos': self.alunos
        }


class Aluno(db.Model):
    __tablename__ = 'Aluno'

    IdAluno = db.Column(db.Integer, primary_key=True)
    NomeAluno = db.Column(db.String(50), unique=False, nullable=False)
    EmailResponsavel = db.Column(db.String(50), unique=False, nullable=False)

    turmas = db.relationship('Turma', secondary='Aluno_Turma', back_populates='alunos', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.IdAluno,
            'nome': self.NomeAluno,
            'email_responsavel': self.EmailResponsavel,
            # 'turmas': self.turmas
        }


class AlunoTurma(db.Model):
    __tablename__ = 'Aluno_Turma'

    idAlunoTurma = db.Column(db.Integer, primary_key=True)
    idAluno = db.Column(db.Integer, db.ForeignKey('Aluno.IdAluno'))
    idTurma = db.Column(db.Integer, db.ForeignKey('Turma.IdTurma'))
