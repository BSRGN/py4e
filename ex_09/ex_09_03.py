#Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, 
#and print the dictionary.
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
    words = words[1]
    email[words] = email.get(words,0) + 1
print(email)