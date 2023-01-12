# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. 
# Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

import re
count = 0
fhand = input('Enter file name: ')
if len(fhand) < 1:
  fhand = 'mbox-short.txt'
hand = open(fhand)
user_input = input('Enter a regular expression: ')
for lin in hand:
  lin = lin.rstrip()
  if re.search(user_input, lin):
    count += 1
print(fhand,'had',count,'lines that matched',user_input)

#Classmate completed program in 2 lines that completed autograder.

#import re
#print(sum([int(i) for i in re.findall('[0-9]+',open('regex_sum_1695380.txt').read())]))