import pyodbc

server = 'DESKTOP-JV5AKTF'
database = 'SYSTEM_PRESENCE'
username = 'sa'
password = 'aplicando@2024guktdhg'

conexao = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
print("Conexão bem-sucedida!")
