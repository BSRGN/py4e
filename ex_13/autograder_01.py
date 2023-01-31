import urllib.request,urllib.parse
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro
serviceurl = ""
if api_key is False:
    api_key = 42
    serviceurl = input('Enter Service URL: ')
    if len(serviceurl) < 1:
        serviceurl = 'http://py4e-data.dr-chuck.net/comments_42.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

parms = dict()
#parms['address'] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

file = urllib.request.urlopen(url)
data = file.read()
#decoding
data = data.decode()
#convert xml file into tree datastructure

tree = ET.fromstring(data)
#print(tree)

#data=tree.find("comments")
comments = tree.findall("comments/")
sum = 0
for comment in comments:
    for i in comment.find("count").text.split("/n"):
        sum += int(i)
counts = tree.findall('.//count')
total = 0
for count in counts:
    total += 1 

print('Count:',total)
print('Sum:',sum)