import socket, threading


serverPort = 9090  # SERVER PORT
clientsAmount = 5  # NUMBER OF CLIENTS

clientsConnections = list()
clientsNames = dict()


def clientHandler(conn, addr):
    print(f"NEW CONNECTION: {addr}")
    conn.send("SYSTEM: Please input your name:".encode("utf-8"))
    clientName = conn.recv(1024).decode("utf-8")
    clientsConnections.append(conn)
    clientsNames[conn] = clientName
    connected = True

    broadcast(conn, f"User {clientName} has joined chat.")
    print(f"{clientName} HAS CONNECTED FROM {addr}")
    print()
    while connected:
        try:
            clientMessage = conn.recv(1024).decode("utf-8")
            if clientMessage:
                print(f"{clientName}: {clientMessage}")
                broadcast(conn, f"{clientName}: {clientMessage}")
        except:
            clientsConnections.remove(conn)
            broadcast(conn, f"User {clientName} has left the chat.")
            print(f"{clientName} FROM {addr} HAS DISCONNECTED")
            print()
            conn.close()
            break

def broadcast(conn, msg):
    for clientConnection in clientsConnections:
        if clientConnection != conn:
            try:
                clientConnection.send(msg.encode("utf-8"))
            except:
                clientConnection.close()
                clientsConnections.remove(clientConnection)
                del clientsNames[clientConnection]


def serverStart(serverPort, clientsAmount):
    serverIp = socket.gethostbyname(socket.gethostname())
    
    print("CLIENTS NEED TO CONNECT TO THIS IP:")
    print("---------------")
    print(serverIp)
    print("---------------")
    print()

    serverSocket = socket.socket()
    serverSocket.bind((serverIp, serverPort))
    serverSocket.listen(clientsAmount)
    print("SERVER IS LISTENING FOR CONNECTIONS")
    print()

    while True:
        conn, addr = serverSocket.accept()
        thread = threading.Thread(target=clientHandler, args=(conn, addr))
        thread.start()
        print(f"ACTIVE CONNECTIONS: {threading.active_count() - 1}")
        print()


serverStart(serverPort, clientsAmount)