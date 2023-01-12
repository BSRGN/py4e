# Autograder: Regular Expressions
# 2 line list comprehension. Same as ex_11_03.py

import re
print(sum([int(i) for i in re.findall('[0-9]+',open('regex_sum_1696631.txt').read())]))