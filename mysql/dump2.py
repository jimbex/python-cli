import socket
import re

d = ""

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)



while True:
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    d = data.decode()
    print(d)
    file = open("dump1.txt", "w")
    files = file.write(d)
mysock.close()