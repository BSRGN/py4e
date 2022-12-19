count = 0
total = 0
while True:
    #string value number
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        #floating point value number
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    print(fval)
    count = count + 1
    total = total + fval
print('ALL DONE')
print('Total: ',total,', Total Count: ',count,', Average: ',total/count)