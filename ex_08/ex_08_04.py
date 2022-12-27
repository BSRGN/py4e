# Find all unique words in a file.
# create a list named unique_words.
unique_words = list()
# Request file input form user.
fhand = input('Enter file name: ')
# Guardian
try:
    fname = open(fhand)
except:
    print("ERROR: Unable to locate file:\n",fhand)
    exit()
# Go through every line in the code putting the split words into "words". 
for line in fname:
    words = line.split()
    # Go through every word in words.
    for word in words:
        # If the word is not in the unique_words list, then append(add) the word to the unique_words list.
        if not word in unique_words:
            unique_words.append(word)
# Sort the unique_words list alphabetically.
unique_words.sort()
print(unique_words)