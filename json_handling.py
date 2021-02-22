"""text file modes"""
import json

data ={
    "id":0,
    "name":"Mau",
    "age":24,
    "position":"Web Developer"
}

data_as_json = json.dumps(data)
print(type(data_as_json))

with open('data.json','w') as json_file:
    json.dump(data,json_file)

with open('data.json','r') as json_file:
    pythonic_jason=json.load(json_file)

print(pythonic_jason)

"""id
email
age
program
score"""

"""id 
email
age
program
score"""

"""investigar
XML to JSON
nombree y apellido"""