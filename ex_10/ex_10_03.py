#Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. 
#Your program should convert all the input to lower case and only count the letters a-z. 
#Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. 
#Find text samples from several different languages and see how letter frequency varies between languages. 
#Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

#import string
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'romeo.txt'
counts = dict()
lst = list()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
try:
    hand = open(fname)
except:
    print('File',fname,'cannot be opened or located.')
    quit()
for line in hand:
    #line = line.strip()
    #line = line.translate(line.maketrans('', '', string.punctuation)) #deletes string puncutation
    line = line.lower() #lower case all letters
    words = line.split() #splits lines into words
    for word in words: #iterates through words
        for letters in word: #iterates through word
            if letters in alphabet: #filters only letters in the variable alphabet(a through z): With this implimented, #import string, #line = line.strip(), and #line = line.translate(line.maketrans('', '', string.punctuation)) are commented out.
                counts[letters] = counts.get(letters,0) +1 #to count letters and place them into dictionary 'counts'
for key, value in counts.items():
    lst.append((value, key)) #place key, value pairs into list 'lst'
lst.sort(reverse=True) #sort list starting with largest
#print(lst) # prints list with tuples
for key, value in lst[:]: #for all key, value pairs in lst
    print(value, key) #prints list 'lst' line by line with value, key
