from socket import *
import sys
import select

host = "127.0.0.1"
port = 9999

s = socket(AF_INET, SOCK_DGRAM)
s.bind((host, port))

addr = (host, port)
buf = 2048

data, addr = s.recvfrom(buf)
print("recibiendo archivo:", data.strip())
f = open("nuevo.mp3",'wb')
data, addr = s.recvfrom(buf)

try:
    while(data):
        f.write(data)
        s.settimeout(2)
        data, addr = s.recvfrom(buf)
except timeout:
    f.close()
    s.close()
    print("Archivo descargado")