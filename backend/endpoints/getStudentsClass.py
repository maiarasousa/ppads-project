import json
from db_connections import db_connection_mysql

def sendRequest(event):
    db = db_connection_mysql.connection()
    cursor = db.cursor()

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