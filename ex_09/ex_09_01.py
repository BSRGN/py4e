#Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are.
#Then you can use the in operator as a fast way to check whether a string is in the dictionary.

#Program to place a text file into a dictionary and prompt user to search for words in said dictionary.
word_dict = dict()
fname = input("Enter File Name: ")
if len(fname) < 1:
    fname = 'words.txt'
try:
    fhand = open(fname)
except:
    print('File',fname,'cannot be opened or located.')
    quit()
for line in fhand:
    line = line.rstrip()
    line = line.split()
    if len(line) == 0:
        #print('Ignore')
        continue
    for w in line:
        word_dict[w] = 1

#print(word_dict)
#print(len(word_dict))

while True:
    search = input(f'Search for a word in the file {fname} OR enter "q" to quit program: ')
    if search == 'q':
        exit()   
    if search in word_dict:
        print('YES,',search,'is in', fname)
    else:
        print(search,'is NOT found in',fname)