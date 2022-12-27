# Function removing first item and last item in a list. Excercise is asking to return 'None'
chop_list = list()
middle_list = list() 
def chop(t):
    del t[0]
    del t[-1]
    return
def middle(t):
    return t[1:len(t)-1]
while True:
    inp = input('Enter number: ')
    if inp == 'done':
        break
    try:
        inp = float(inp)
        chop_list.append(inp)
        middle_list.append(inp)
    except:
        continue
middle_list.sort()
chopped = chop(chop_list)
middled = middle(middle_list)
print('Chop:',chopped)
print('Middle:',middled)