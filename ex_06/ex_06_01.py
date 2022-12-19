#Enter a word and print out each letter individually backwards.
word = input('Enter word to print out backwards: ')
index = -1
for letter in word:
  letter = word[index]
  print(letter)
  index -= 1
print('Fin')