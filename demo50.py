# encoding=UTF-8
import requests

base_url = 'https://py20190618.firebaseio.com/%s.json'
url4 = base_url % 'demo4'
url5 = base_url % 'demo5'
url99=base_url % 'demo99'

json4 = {'3': 'The North ', '1': 99415, '6': u'獅子', '7': u'Winter is coming', '4': 'dog and cat'}
result4 = requests.patch(url4, json=json4)
print result4.status_code, result4.content

json5 = {'instructor': 'Snow', 'duration': 36, 'King': 'Lady Sansa'}
result5 = requests.patch(url5, json=json5)
print result5.status_code, result5.content

json99 = {'instructor': 'Snow', 'duration': 999936, 'King': 'Lady Sansa999'}
result99 = requests.patch(url99, json=json99)
print result99.status_code, result99.content
