# Copy and paste terminal address: and python program below:

# cd /Users/michaelbasargin/Documents/Github/py4 
# python3 python_playground.py

# import random

# for i in range(10):
#    x = random.random()
#    print(x)

#x =  [1,2,3,4,5]
#x = list(range(5))
#print(x)

#stuff = dict()
#print(stuff.get('candy',-1))

#txt = 'but soft what light in yonder window breaks'
#words = txt.split()
#t = list()
#for word in words:
#    t.append((len(word), word))
#    print('***1***',t)
#
#t.sort(reverse=True)
#print('***2***',t)
#res = list()
#for length, word in t:
#    res.append(word)
#
#print('***3***',res)

inp = input('enter file:')
try: fhand = open(inp)
except:
    print ('try again')
    exit()
#import string
alphabet = 'abcdefghijklmnopqrstuvwxyz'
dct = dict()
for line in fhand:
    #line = line.strip()
    #line = line.translate(str.maketrans('','', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            if letter in alphabet:
                dct[letter] = dct.get(letter,0) + 1
Lst = list()            #rearranging from most to least
for key,value in dct.items():
    Lst.append([value,key])
Lst.sort(reverse=True)
print (Lst)