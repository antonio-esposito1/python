#!/usr/bin/python3.9

if __name__== "__main__":
 import json
 with open('json_example.json', 'r') as file:
    data = json.load(file)
 print(data)
 print(type(data))
 user = data['user']
 print(user)
 print(type(user))
 print(user['name'])
 for role in user['roles']:
    print(role)
 user['location']['city'] = 'Dallas'
 with open('json_example-edit.json', 'w') as file:
    json.dump(data,file, indent=4)
print(data)
