from urllib.request import urlopen
import json
url = "https://jsonplaceholder.typicode.com/posts"
response = urlopen(url)
data = json.loads(response.read())
print(data)