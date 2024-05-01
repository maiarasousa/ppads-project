import json
from datetime import datetime
from db_connections import db_connection_mysql

def sendRequest(event):
    db = db_connection_mysql.connection()
    cursor = db.cursor()

    listPresence = json.loads(event["body"])
    for student in listPresence:
        query = f"""
            insert into Frequency (idStudent, idClass, idTeacher, calledDate, presenceStatus, typeCalled)
            values ({student["idStudent"]}, {student["idClass"]}, 1, '{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}', {student["presenceStatus"]}, {student["typeCalled"]})
        """

        cursor.execute(query)
        db.commit()

    return {
        "statusCode": 200,
        "headers": { 'Access-Control-Allow-Origin': '*' },
        "body": json.dumps({ "Message": "Lista de presença salva com sucesso!" })
    }   