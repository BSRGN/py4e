# Autograder: Extract Data from JSON

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = input('Input url: ')
if len(serviceurl) < 1:
    serviceurl = 'http://py4e-data.dr-chuck.net/comments_42.json'

di = dict()
# Parses serviceurl, encodes it to be readable, then places it into dictionary 'di'.
url = serviceurl + urllib.parse.urlencode(di)
print('Retrieving', url)
uh = urllib.request.urlopen(url)
read = uh.read()
print('Retrieved', len(read), 'characters')
# .loads stands for "load string" and you get a Python list [].
js = json.loads(read)
# json.dumps formats the json file and indents it by 4 spaces for readability.
data = json.dumps(js, indent = 4)
#print(data)

count = 0
sum = 0
count_di = dict()

for names in js['comments']:
    sum += int(names['count'])
    count_di[count] = count_di.get(count,0) +1
    
print('Count:', count_di[count])
print('Sum:', sum)