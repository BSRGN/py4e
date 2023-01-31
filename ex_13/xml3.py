# It is important to include all parent level elements in the findall statement except for the top level element (e.g., users/user). Otherwise, Python will not find any desired nodes.
import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)

# Print(len(lst)) = User count: 2
# Count is 2 because both parent and child were included in the findall.
lst = stuff.findall('users/user')
print('User count:', len(lst))

# Print(len(lst2)) = User count: 0
# Count was 0 because the parent of child 'user' was not included in the findall. Include the parent to find child nodes.
lst2 = stuff.findall('user')
print('User count:', len(lst2))
