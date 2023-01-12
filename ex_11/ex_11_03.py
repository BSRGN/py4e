# Handling The Data 
# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' 
# and then converting the extracted strings to integers and summing up the integers.

import re
total = 0
num = 0
fhand = input('Enter file name: ')
if len(fhand) < 1:
  fhand = 'regex_sum_42.txt'
try:
    hand = open(fhand)
except:
  print('File',fhand,'cannot be opened or located.')
  quit()
for lin in hand:
  lin = lin.rstrip()
  x = re.findall('([0-9]+)', lin)
  if len(x) > 0:
    #print(x)
    #print(type(x))
    for number in x:
        number = int(number[:])
        #print(number)
        total += number
print(total)