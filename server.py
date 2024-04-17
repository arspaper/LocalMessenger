import socket


serverPort = 9090  # SERVER PORT
serverName = "server"  # SERVER NAME
clientsAmount = 5  # NUMBER OF CLIENTS

def serverStart(serverPort, serverName, clientsAmount):
    serverIp = socket.gethostbyname(socket.gethostname())
    
    print("CLIENTS NEED TO CONNECT TO THIS IP:")
    print("---------------")
    print(serverIp)
    print("---------------")

    mySocket = socket.socket()
    mySocket.bind((serverIp, serverPort))

    mySocket.listen(clientsAmount)

serverStart(serverPort, serverName)