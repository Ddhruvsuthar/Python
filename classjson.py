import json
 
class User:
    def __init__(self , name , age):
        self.name = name
        self.age = age 

user = User('Max',27)

def encode_user(o):
        if isinstance(o,User):
            return{'name': o.name,'age':o.age,       o.__class__.__name__:True}
        else:
            raise TypeError('Wrong fuck you')

userJSON = json.dumps(user, default=encode_user)
print(userJSON)