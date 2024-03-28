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
	EmailResponsavel varchar(50) NOT NULL,
	IdTurma int NOT NULL FOREIGN KEY REFERENCES Turma(IdTurma)
);

CREATE TABLE Professor (
	IdProfessor int NOT NULL PRIMARY KEY,
	NomeProfessor varchar(50) NOT NULL,
	EmailProfessor varchar(50) NOT NULL,
	IdTurma int NOT NULL FOREIGN KEY REFERENCES Turma(IdTurma)
);

CREATE TABLE Frequencia (
	IdFrequencia int NOT NULL PRIMARY KEY,
	DataChamada date NOT NULL,
	Presente BIT NOT NULL,
	IdTurma int NOT NULL FOREIGN KEY REFERENCES Turma(IdTurma),
	IdProfessor int NOT NULL FOREIGN KEY REFERENCES Professor(IdProfessor),
	IdAluno int NOT NULL FOREIGN KEY REFERENCES Aluno(IdAluno)
);

CREATE TABLE Notificacoes (
	IdNotificacoes int NOT NULL PRIMARY KEY,
	DataNotificacao date NOT NULL,
	IdTurma int NOT NULL FOREIGN KEY REFERENCES Turma(IdTurma),
	IdProfessor int NOT NULL FOREIGN KEY REFERENCES Professor(IdProfessor),
	IdAluno int NOT NULL FOREIGN KEY REFERENCES Aluno(IdAluno)
);

INSERT INTO Turma VALUES 
(9999, 'Turma 1', 2024),
(9998, 'Turma 2', 2024),
(9997, 'Turma 3', 2024);

INSERT INTO Aluno VALUES
(8888, 'Monique', 'teste@teste.com', 9999),
(8887, 'Susane', 'teste@teste.com', 9999),
(8886, 'Pedro', 'teste@teste.com', 9999),
(8885, 'Monique', 'teste@teste.com', 9998),
(8884, 'Susane', 'teste@teste.com', 9998),
(8883, 'Pedro', 'teste@teste.com', 9998),
(8882, 'Monique', 'teste@teste.com', 9997),
(8881, 'Susane', 'teste@teste.com', 9997),
(8880, 'Pedro', 'teste@teste.com', 9997);

INSERT INTO Professor VALUES
(7777, 'Joao', 'teste@teste.com', 9999),
(7776, 'Maria', 'teste@teste.com', 9999),
(7775, 'Jose', 'teste@teste.com', 9998),
(7774, 'Joana', 'teste@teste.com', 9998),
(7773, 'Pedro', 'teste@teste.com', 9997),
(7772, 'Lucia', 'teste@teste.com', 9997);