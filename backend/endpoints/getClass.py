import json
from db_connections import db_connection_mysql

def sendRequest(event):
    db = db_connection_mysql.connection()
    cursor = db.cursor()

    query = "SELECT * FROM Class"
    cursor.execute(query)
    resultados = cursor.fetchall()

    lista_json = []
    for linha in resultados:
        dicionario = {
            'idClass': linha[0],
            'yearSchool': linha[1],
            'className': linha[2]
        }
        lista_json.append(dicionario)

    return {
        "statusCode": 200,
        "headers": { 'Access-Control-Allow-Origin': '*' },
        "body": json.dumps(lista_json)
    }