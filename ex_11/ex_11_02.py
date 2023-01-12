# Exercise 2: Write a program to look for lines of the form: "New Revision: 39772".
# Extract the number from each of the lines using a regular expression and the findall() method.
# Compute the average of the numbers and print out the average as an integer.

import re
count = 0
total = 0
fhand = input('Enter file name: ')
if len(fhand) < 1:
  fhand = 'mbox.txt'
try:
    hand = open(fhand)
except:
  print('File',fhand,'cannot be opened or located.')
  quit()
for lin in hand:
  lin = lin.rstrip()
  x = re.findall('New Rev.+\S: ([0-9.]+)', lin)
  if len(x) > 0:
    count += 1
    #print(type(x))
    lst = x[0]
    integer = int(lst)
    total += integer
average = total/count
print(int(average))