# encoding=UTF-8
import requests

base_url = 'https://py20190618.firebaseio.com/%s.json'

url6 = base_url % 'demo6'

for x in range(0, 10):
    message6 = {'title': 'first message', 'id': x *2 }
    result6 = requests.post(url6, json=message6)
    print result6.status_code, result6.content