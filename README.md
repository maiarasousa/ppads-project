# Sistema de Presença

## Descrição:

O **Sistema de Presença** é uma aplicação web desenvolvida para facilitar o processo de realização de chamadas em escolas. A aplicação permite que os professores registrem a presença dos alunos de forma rápida e eficiente.

## Tecnologias utilizadas:
Implantação Cloud:
- Lambda AWS
- API Gateway AWS
- RDS AWS - MySQL
- S3 Bucket AWS

Desenvolvimento:
- Python
- HTML
- JavaScript
- CSS
- Bootstrap
- Swagger

## Pré-requisitos:

- Conexão à internet

## Como utilizar:

1. Acesse o link: [https://system-presence.s3.amazonaws.com/frontend/index.html](https://system-presence.s3.amazonaws.com/frontend/index.html)
4. Na página inicial, clique em "Presença" no menu lateral.
5. Selecione a turma e o horário da chamada.
6. Marque a presença ("Sim") ou a ausência ("Não") de cada aluno.
7. Clique em "Confirmar" para salvar a lista de presença.

## Opções adicionais:

- **Cancelar a chamada:** clique em "Cancelar" para retornar à tela de chamada.
- **Desistir do cancelamento:** clique em "Continuar" para voltar à página inicial.

## Documentação da API:

[Swagger API Documentation](https://app.swaggerhub.com/apis-docs/sousa8/system-presence/2024-04-01#/default/post_postListPresence)
