import sys
import socket

cliente = []
datoscliente = ''

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('172.18.0.2', 8080)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# escuchando las conexiones entrantes
sock.listen(3)

while True:
    #esperando una conexion 
    print("esperando una conexion")
    connection,client_address = sock.accept()
    try:
        print("conexion de ", client_address)
        # Recibir los datos en pequeños fragmentos y retransmitirlos 
        while True:
            data = connection.recv(160)
            if data:
                if(data.decode("UTF-8") =='get clients'):
                    listaclientes = ''
                    for datoscliente in cliente:
                        listaclientes += datoscliente+','
                    print(listaclientes)
                    connection.sendall(listaclientes.encode())
                else:
                    print('recibido {!r}'.format(data))
                    if(cliente == []):
                        cliente.append(data.decode("UTF-8"))
                        print("almacenado: ",cliente)
                    else:
                        for x in range(len(cliente)):
                            if(cliente[x]== data.decode("UTF-8")):
                                print("Este Servidor ya esta registrado")
                                break
                            else:
                                cliente.append(data.decode("UTF-8"))
                                print("almacenado: ",cliente)
            else:
                #print('no hay datos de ',client_address)
                break
    finally:
        connection.close()