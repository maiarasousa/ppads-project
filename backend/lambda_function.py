import json
import mysql.connector

from datetime import datetime
from db_connections import db_connection_mysql

def lambda_handler(event, context):
    print('EVENT')
    print(event)
    print(context)
    
    db = db_connection_mysql.connection()
    cursor = db.cursor()
        
    if(event['resource'] == '/getClass'):
        print('Recebi um: /getClass')
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
       
    if(event['resource'] == '/getStudentsClass'):
        print('Recebi um: /getStudentsClass') 
        query = f"""
            select cl.idClass,
	        st.idStudent, st.nameStudent
            from Student st
            inner join Class cl
            on st.idClass = cl.idClass
            where st.idClass = {event['queryStringParameters']['idClass']}
        """
        cursor.execute(query)
        resultados = cursor.fetchall()
    
        lista_json = []
        for linha in resultados:
            dicionario = {
                'idClass': linha[0],
                'idStudent': linha[1],
                'nameStudent': linha[2]
            }
            lista_json.append(dicionario)
    
        return {
            "statusCode": 200,
            "headers": { 'Access-Control-Allow-Origin': '*' },
            "body": json.dumps(lista_json)
        }
    
    if(event['resource'] == '/postListPresence'):
        print('Recebi um: /postListPresence')
         
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
 