# Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. 
# The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.

import urllib.request, urllib.parse, urllib.error

url = input('Enter a website url: ')
try:
  fhand = urllib.request.urlopen(url)#.read()

except:
  print('Cannot connect the url:',url)
  quit()
total = 0
counts = dict()
for lin in fhand:
  words = lin.decode().split()
  for word in words:
    for letters in word:
      counts[letters] = counts.get(letters, 0) + 1
#print(counts)
lst = list()
for key,value in counts.items():
  lst.append((value,key))
lst.sort(reverse=True)
#print(lst)
for key,value in lst:
  total += key
  #print(key, value) #prints all key and values on print line.
 

print('\n\n   Total number of characters in:',url,'\n  ',total,'characters')