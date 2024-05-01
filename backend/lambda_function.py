import json
from endpoints import getClass
from endpoints import getStudentsClass
from endpoints import postListPresence
from endpoints import postStudent
from endpoints import postTeacher
from endpoints import postClass

def lambda_handler(event, context):    
    if(event['resource'] == '/getClass'):
        return getClass.sendRequest(event)
       
    if(event['resource'] == '/getStudentsClass'):
        return getStudentsClass.sendRequest(event)
    
    if(event['resource'] == '/postListPresence'):
        return postListPresence.sendRequest(event)
    
    if(event['resource'] == '/postStudent'):
        return postStudent.sendRequest(event)
    
    if(event['resource'] == '/postTeacher'):
        return postTeacher.sendRequest(event)
 
    if(event['resource'] == '/postClass'):
        return postClass.sendRequest(event)