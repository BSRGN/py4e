#Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, 
#look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.
fname = input('Enter file name: ')
if len(fname) < 1:
  fname = 'mbox-short.txt'
count = dict()
try:
  fhand = open(fname)
except:
  print('File',fname,'cannot be opened or located.')
  quit()
for lines in fhand:
  words = lines.split()
  if not lines.startswith('From '):
    continue
  words = lines.split()
  if len(words) < 3:
    continue
  word = words[1]
  count[word] = count.get(word,0) + 1
#print(count)
maxnum = None
maxmail = None
for email,x in count.items():
  if maxnum == None:
    maxnum = x
    maxmail = email
  elif maxnum < x:
    maxnum = x
    maxmail = email
print(maxmail,maxnum)