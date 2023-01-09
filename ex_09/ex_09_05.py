#Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from 
#(i.e., the whole email address). At the end of the program, print out the contents of your dictionary.
fname = input('Enter file name: ')
if len(fname) < 1:
  fname = 'mbox-short.txt'
di = dict()
try:
  fhand = open(fname)
except:
  print('File',fname,'cannot be opened or located.')
  quit()
for lines in fhand:
  lines = lines.rstrip()
  words = lines.split()
  #print('***1***',words)
  if not lines.startswith('From '):
    continue
  words = lines.split()
  if len(words) < 3:
    continue
  #print('***2***',words)
  words = words[1].split('@')
  #print('***3***',words)
  word = words[1]
  di[word] = di.get(word,0) + 1
print(di)