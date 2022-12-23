# Read text files
fname = input('Enter the file name: ')
count = 0
float_count = 0
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
for line in fhand:
    # Removes white space from right side
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        ipos = line.find(":")
        string_num = line[ipos+1:]
        float_num = float(string_num)
        float_count = float_count + float_num
        avg = float_count/count
print('Average spam confidence:', avg)