# Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”.
# Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the 
# loop completes.
num = list()
while True:
    inp = input('Enter number: ')
    if inp == 'done':
        break
    inp = int(inp)
    num.append(inp)  
maximum = max(num)
minimum = min(num)
f_maximum = float(maximum)
f_minimum = float(minimum)
print('Maximum:', f_maximum)
print('Minimum:', f_minimum)