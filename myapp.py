import requests
import os
import json

URL="http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data={}
    if id is not None:
        data={'id':id}
    json_data =json.dumps(data)
    r=requests.get(url=URL, data =json_data)

    data=r.json()
    print(data)
#get_data(2) #read
def post_data():
    data ={
        'name':'satya',
        'roll':129,
        'city':'Goa',

    }
    json_data=json.dumps(data)
    
    r=requests.post(url=URL, data =json_data)

    data=r.json()
    print(data)
post_data()
def updata_data():
    data ={
        'id':1,
        'name':'prasanta',
        'city':'Mumbai',

        

    }
    json_data=json.dumps(data)
    
    r=requests.put(url=URL, data =json_data)

    data=r.json()
    print(data)
#updata_data()
def delete_data():
    data ={'id': 4 }
    json_data=json.dumps(data)
    
    r=requests.delete(url=URL, data =json_data)

    data=r.json()
    print(data)
#delete_data()