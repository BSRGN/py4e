# Following Links in Python
# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
# The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, 
# scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter website url: ')
position = input('Enter position location of the name: ')
position_int = int(position)
count = input('Enter number of hyperlinks to parse: ')
count_int = int(count)

name = None
while count_int > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    tag = tags[position_int-1]
    url = tag.get('href', None)
    print('Retrieving:',url)
    name = tag.text
    count_int -= 1
print(f'{name} is at the number {position} position after {count} link(s).')