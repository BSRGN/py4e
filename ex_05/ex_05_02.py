largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        number = int(num)
    except:
        print("Invalid input")
        continue
    if largest is None or number > largest:
            largest = number
    if smallest is None or number < smallest:
            smallest = number

print("Maximum is", largest)
print("Minimum is", smallest)