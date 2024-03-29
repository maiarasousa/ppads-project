from flask_sqlalchemy import SQLAlchemy
from db import db

class Turma(db.Model):
    __tablename__ = 'Turma'

    IdTurma = db.Column(db.Integer, primary_key=True)
    NomeTurma = db.Column(db.String(50), unique=False, nullable=False)
    AnoLetivo = db.Column(db.Integer, unique=False, nullable=False)

    def to_dict(self):
        return {
            'idTurma': self.IdTurma,
            'nomeTurma': self.NomeTurma,
            'anoLetivo': self.AnoLetivo
        }

 