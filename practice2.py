import json 
f = open('samplejsonfile.json',)
data = json.load(f)
print(data[0]['color'])
print(data[0]['value'])


for i in data:
    print(i)
f.close()    

