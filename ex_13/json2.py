import json

# ''' groups all data inbetween the triple two sets of '''.
# the "data" variable below has two dictionaries {} seperated by a comma inside of a list [].
data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

# .loads stands for "load string" and you get a Python list [].
info = json.loads(data)
print('User count:', len(info))

# for loops prints type: 'str'.
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

# Code: http://www.py4e.com/code3/json2.py