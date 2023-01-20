# Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page. You can use split('/') to break the URL into its component parts
# so you can extract the host name for the socket connect call. Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.

import socket

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
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()