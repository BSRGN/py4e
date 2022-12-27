# Write a program to read through the mail box data and when you find line that starts with “From”, you will split the line into words using the split function.
# We are interested in who sent the message, which is the second word on the From line.
# You will parse the From line and print out the second word for each From line, 
# then you will also count the number of From (not From:) lines and print out a count at the end.
count = 0
fhand = input('Enter file name: ')
try:
    fname = open(fhand)
except:
    print('ERROR: Unable to locate file name:\n',fhand)
    exit()
for line in fname:
    # Removes the white space from the right side of the line.
    line = line.rstrip()
    # If the length of the line is none; as in the line is blank, then skip this line and continue.
    if len(line) == 0:
        continue
    # If the line starts with the word From, add 1 to the count variable, split the words in the line that have a space, and print the second word in the line
    # which is line[1] since line[0] would be the first word
    if line.startswith('From '):
        count += 1
        line = line.split()
        print(line[1])
print('There were',count, 'lines in the file with From as the first word')