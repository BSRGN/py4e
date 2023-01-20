# Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. 
# The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.

import urllib.request

url = input('Enter a website url: ')
try:
  fhand = urllib.request.urlopen(url).read()

except:
  print('Cannot connect the website url:',url)
  quit()

fname = fhand[:3000].decode()
print(fname)
  
characters = len(fname)

print('\n\n   Total number of characters in:',url,'\n  ',characters,'characters')