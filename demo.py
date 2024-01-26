import json

person={'haschildren':False,'name' : 'Dhruv' ,'age':21, 'city': 'udaipur', }
personJSON=json.dumps(person, indent=4)

#print (personJSON)

with open('demo.json', 'r') as file:
    personpython=json.loads(personJSON,)
    print(personpython)

