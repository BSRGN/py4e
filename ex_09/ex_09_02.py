#Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, 
#then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary 
#(order does not matter).
fname = input('Enter file name: ')
if len(fname) < 1:
  fname = 'mbox-short.txt'
email = dict()
try:
  fhand = open(fname)
except:
  print('File',fname,'cannot be opened or located.')
  quit()
for lines in fhand:
    lines = lines.rstrip()
    words = lines.split()
    if len(words) < 3 or words[0] != 'From':
      continue
    words = words[2]
    email[words] = email.get(words,0) + 1
print(email)