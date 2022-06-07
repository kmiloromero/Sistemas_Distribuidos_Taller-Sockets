import socket
import sys

# se inicializa socket servidor
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conexion del servidor al index 

port = 8081
ip = '172.18.0.3'

server_address = ('172.18.0.2', 8080)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
#MOSTRAR LISTA DE CLIENTES 
message= str(port)+ip+"Randon"
print('sending '+message)
sock.sendall(message.encode())
sock.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Se inicializa el servidor

server_address2 = (ip,port)
print('starting up on {} port {}'.format(*server_address2))
print(server_address2)
sock.bind(server_address2)

# en espera de conexiones
sock.listen(1)

while True:
    # esperando conexion
    print('esperando una conexion')
    connection, client_address = sock.accept()
    try:
        print('conexion de', client_address)
        while True:
            data = connection.recv(160)
            print('recibio {}'.format(data))
            break
    finally:
        connection.close()