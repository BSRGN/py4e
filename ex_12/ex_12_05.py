# Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers and a blank line have been received. 
# Remember that recv receives characters (newlines and all), not lines.

import socket
import time

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
mysock.sendall(cmdstr.encode())
count = 0
ptxt = b""

while True:
    data = mysock.recv(5120)
    if len(data) < 1:
      break
    time.sleep(0.25)
    count = count + len(data)
    ptxt = ptxt + data
mysock.close()

# Search for the end of the header (2 CRLF)
pos = ptxt.find(b"\r\n\r\n")

# Skip past the header and save the ptxt data
ptxt = ptxt[pos+4:]
print(ptxt.decode())