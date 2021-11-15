from urllib.request import urlopen
import json
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)





url = "https://jsonplaceholder.typicode.com/posts"
response = urlopen(url)
data = json.loads(response.read())
jprint(data)