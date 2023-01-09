#Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line.
#Count the number of messages from each person using a dictionary.

#After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary.
#Then sort the list in reverse order and print out the person who has the most commits.

fname = input('Enter file name: ')
if len(fname) < 1:
  fname = 'mbox-short.txt'
di = dict()
try:
  hand = open(fname)
except:
  print('File',fname,'cannot be opened or located.')
  quit()
for lin in hand:
  lin = lin.rstrip()
  wds = lin.split()
  #print('***1***',wds)
  if not lin.startswith('From '):
    continue
  wds = lin.split()
  if len(wds) < 3:
    continue
  wds = wds[1]
  di[wds] = di.get(wds,0) +1
  #print('***2***',wds)
#print(di)
l = list()
for count,email in di.items():
  l.append((email,count))
l.sort(reverse=True)
#print(l)
for count, email in l[:1]:
  print(email, count)