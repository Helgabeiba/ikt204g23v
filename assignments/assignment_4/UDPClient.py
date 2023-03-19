from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
strMessage = input('Input lowercase sentence: ')
byteMessage = bytearray(strMessage, 'utf-8')
clientSocket.sendto(byteMessage, (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode('utf-8'))
clientSocket.close()