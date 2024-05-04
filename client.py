import socket, threading


serverIp = input("Please input server IP")
serverPort = int(input("Please input server port"))


def messageRecieve(sock):
    while True:
        try:
            foreignMessage = sock.recv(1024).decode('utf-8')
            if foreignMessage:
                print(foreignMessage)
        except:
            print("SYSTEM: You have been disconnected from the server.")
            print()
            sock.close()
            break

def messageSend(sock):
    while True:
        message = input('')
        sock.send(message.encode('utf-8'))


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect((serverIp, serverPort))

threadRecv = threading.Thread(target=messageRecieve, args=(mySocket,))
threadRecv.start()

threadSend = threading.Thread(target=messageSend, args=(mySocket,))
threadSend.start()