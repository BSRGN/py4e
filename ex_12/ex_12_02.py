# Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. 
# The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.

import socket
import time
count = 0
input_url = input('Input website url address: ')
try:
  url = input_url.split('/')[2]
except:
  print('Bad url input: ',input_url)
  quit()
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  mysock.connect((url, 80))
except:
  print('Unable to connect: ',input_url)
  quit()
cmdstr = 'GET %s HTTP/1.0\r\n\r\n' %input_url
cmd = cmdstr.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(3000)
    if len(data) < 1:
      break
    time.sleep(0.25)
    count = count + len(data)
    if count <= 3000:
      print(data.decode(),end='')
print('\nFile length:',count)

mysock.close()