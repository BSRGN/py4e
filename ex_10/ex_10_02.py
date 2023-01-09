#Exercise 2: This program counts the distribution of the hour of the day for each of the messages. 
#You can pull the hour from the “From” line by finding the hour string and then splitting that string into parts using the colon character.
#Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

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
  #print('***Debug***',wds)
  wds = wds[5]
  time = wds.split(':')
  hour = time[0]
  #print('***Debug***',hour)
  di[hour] = di.get(hour,0) +1
  #print('***2***',wds)
#print(di)
l = list()
for count,hour in di.items():
  l.append((count,hour))
l.sort()
#print(l)
for count, hour in l[:]:
  print(count, hour)