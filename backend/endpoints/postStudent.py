import json
from datetime import datetime
from db_connections import db_connection_mysql

def sendRequest(event):
    db = db_connection_mysql.connection()
    cursor = db.cursor()

    student = json.loads(event["body"])

    query = f"""
        insert into Student (idClass, nameStudent, responsableEmail)
        values ({student["idClass"]}, '{student["nameStudent"]}', '{student["responsableEmail"]}')
    """

    cursor.execute(query)
    db.commit()

    return {
        "statusCode": 200,
        "headers": { 'Access-Control-Allow-Origin': '*' },
        "body": json.dumps({ "Message": "Aluno cadastrado com sucesso!" })
    }