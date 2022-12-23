# Read text files
fname = input('Enter the file name: ')
count = 0
if fname == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
for line in fhand:
    # Removes white space from right side
    line = line.rstrip()
    # Skips lines that do not start with 'From:'
    if line.startswith('Subject:'):
        count += 1
print('There were',count,'subject lines in',fname)