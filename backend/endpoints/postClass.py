import json
from datetime import datetime
from db_connections import db_connection_mysql

def sendRequest(event):
    db = db_connection_mysql.connection()
    cursor = db.cursor()

    classs = json.loads(event["body"])

    query = f"""
        insert into Class (yearScholl, className)
        values ({classs["yearScholl"]}, '{classs["className"]}')
    """

    cursor.execute(query)
    db.commit()

    return {
        "statusCode": 200,
        "headers": { 'Access-Control-Allow-Origin': '*' },
        "body": json.dumps({ "Message": "Turma cadastrada com sucesso!" })
    } 