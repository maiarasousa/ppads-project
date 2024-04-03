import json
from endpoints import getClass
from endpoints import getStudentsClass
from endpoints import postListPresence

def lambda_handler(event, context):    
    if(event['resource'] == '/getClass'):
        return getClass.sendRequest(event)
       
    if(event['resource'] == '/getStudentsClass'):
        return getStudentsClass.sendRequest(event)
    
    if(event['resource'] == '/postListPresence'):
        return postListPresence.sendRequest(event)
 