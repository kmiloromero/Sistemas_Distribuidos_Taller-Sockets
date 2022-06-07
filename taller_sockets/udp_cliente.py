from socket import *
import sys

s = socket(AF_INET, SOCK_DGRAM)
ip = "127.0.0.1"
puerto = 9999
buf = 2048
addr = (ip, puerto)

file_name = "Audio.mp3"

f = open(file_name,"rb")
data = f.read(buf)

s.sendto(data, addr)
while (data):
    if(s.sendto(data, addr)):
        print("enviando...")
        data = f.read(buf)
s.close()
f.close()