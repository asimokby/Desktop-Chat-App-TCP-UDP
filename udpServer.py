
import socket

 

localIP = "127.0.0.1"

localPort   = 20001

bufferSize  = 1024

 

msgFromServer = "Hello UDP Client"

bytesToSend = str.encode(msgFromServer)

 

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

 

print("UDP server up and listening")

 
#list of clients 
clients = {}


# Listen for incoming datagrams
while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    # message
    address = bytesAddressPair[1]

    #TODO  append only if they are not in the list
    exists = False
    for c in clients: 
        if c[1] == address[1]:
            exists = True

    if not exists:
        clients[address] = message
        continue # do not send names to clients


    name = ''
   #getting the name of the sender 
    for c in clients: 
        if c[1] == address[1]:
            name = clients[address]

   

    # Sending a reply to client
    print(clients)
    for c in clients:
        if c[1] != address[1]:
            UDPServerSocket.sendto(name + b'>>' + message, c)