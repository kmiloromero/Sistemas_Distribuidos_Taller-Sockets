import socket
import sys

# se crea socket tcp/ip
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('172.18.0.2', 8080)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

#MOSTRAR LISTA DE CLIENTES 
message="get clients"
print('sending '+message)
sock.sendall(message.encode())
data = sock.recv(160)
print('recibido{!r}'.format(data))
sock.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = input('ingrese la ip del servidor: ')
puerto = int(input("ingrese el puerto del servidor: "))
server_address2 = (ip, puerto)

# conecta el socket al puerto donde el servidor esta escuchando
print('conectando a puerto {} port {}'.format(*server_address2))
sock.connect(server_address2)
try:
    while True:
        # envio de datos
        message = input("ingrese su mensaje:")
        print('enviado{!r}'.format(message))
        sock.sendall(message.encode())
        break
finally:
    print('cerrando socket')
    sock.close()