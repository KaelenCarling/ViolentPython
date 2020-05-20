import socket

services = {'ftp': 21, 'ssh': 22, 'smtp': 25, 'http': 80}

socket.setdefaulttimeout(2)

soc = socket.socket()

soc.connect(('193.235.51.116', 443))

ans = soc.recv(1024)

print(ans)