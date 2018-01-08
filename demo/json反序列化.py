import json

f = open('json.txt','r')

data = json.load(f)

print(data)