import json

data = {'name':'fingal','agx':19}

f = open('json.txt','w+')

f.write(json.dumps(data))

f.close()
