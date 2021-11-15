import json
weather = urllib2.urlopen('url')
wjson = weather.read()
wjdata = json.loads(wjson)
print wjdata['data']['current_condition'][0]['temp_C']


from urllib.request import urlopen
import json
url = "https://jsonplaceholder.typicode.com/posts"
response = urlopen(url)
data = json.loads(response.read())
print(data)