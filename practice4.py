import json
ar = '{"good":["a","b","c","d"]}'

data = json.loads(ar)
print(data['good'])