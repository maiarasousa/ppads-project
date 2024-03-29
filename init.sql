CREATE DATABASE SystemPresence
GO

USE SystemPresence 
GO

CREATE TABLE Turma (
	IdTurma int NOT NULL PRIMARY KEY,
	NomeTurma varchar(50) NOT NULL,
	AnoLetivo int NOT NULL
)
GO

CREATE TABLE Aluno (
	IdAluno int NOT NULL PRIMARY KEY,
	NomeAluno varchar(50) NOT NULL,
	EmailResponsavel varchar(50) NOT NULL
)
GO

CREATE TABLE Aluno_Turma (
	IdAlunoTurma int NOT NULL PRIMARY KEY,
	IdTurma int NOT NULL FOREIGN KEY REFERENCES Turma(IdTurma),
	IdAluno int NOT NULL FOREIGN KEY REFERENCES Aluno(IdAluno)
)
GO

CREATE TABLE Professor (
	IdProfessor int NOT NULL PRIMARY KEY,
	NomeProfessor varchar(50) NOT NULL,
	EmailProfessor varchar(50) NOT NULL
)
GO

CREATE TABLE Frequencia (
	IdFrequencia int NOT NULL PRIMARY KEY,
	DataChamada date NOT NULL,
	Presente BIT NOT NULL
)
GO

CREATE TABLE Notificacoes (
	IdNotificacoes int NOT NULL PRIMARY KEY,
	DataNotificacao date NOT NULL,
	IdTurma int NOT NULL FOREIGN KEY REFERENCES Turma(IdTurma),
	IdProfessor int NOT NULL FOREIGN KEY REFERENCES Professor(IdProfessor),
	IdAluno int NOT NULL FOREIGN KEY REFERENCES Aluno(IdAluno)
)
GO

INSERT INTO Turma VALUES 
(9999, 'Turma 1', 2024),
(9998, 'Turma 2', 2024),
(9997, 'Turma 3', 2024);

INSERT INTO Aluno VALUES
(8888, 'Monique', 'teste@teste.com'),
(8887, 'Susane', 'teste@teste.com'),
(8886, 'Pedro', 'teste@teste.com');

INSERT INTO Aluno_Turma VALUES
(6666, 9999, 8888),
(6665, 9999, 8887),
(6664, 9999, 8886),
(6663, 9998, 8888),
(6662, 9998, 8887),
(6661, 9998, 8886),
(6660, 9997, 8888),
(6659, 9997, 8887),
(6658, 9997, 8886);

INSERT INTO Professor VALUES
(7777, 'Joao', 'teste@teste.com'),
(7776, 'Maria', 'teste@teste.com'),
(7775, 'Jose', 'teste@teste.com'),
(7774, 'Joana', 'teste@teste.com'),
(7773, 'Pedro', 'teste@teste.com'),
(7772, 'Lucia', 'teste@teste.com');