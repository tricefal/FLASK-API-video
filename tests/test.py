import requests

BASE_URL = '127.0.0.1:5000/'

response = requests.put(BASE_URL + 'video/%d' % 1, {
	"views": 125,
	"likes" : 86,
})

print(response.json())

