# Rewrite the guardian program fromm ex_08_02.py without two if statments.
# Instead, use a compund logical expression using the or logical operator with a single if statment.
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    if len(words) == 0 or words[0] != 'From':
        continue
    print(words[2])