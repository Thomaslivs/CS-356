#Thomas Livshits
#tl263
#CS 356-002

#Server

import sys #SocketAPI PowerPoint
from socket import * #SocketAPI PowerPoint
from random import *
from struct import * #SocketAPI PowerPoint
serverIP = "127.0.0.1" #SocketAPI PowerPoint
serverPort = 12000 #SocketAPI PowerPoint
dataLen = 1000000 #SocketAPI PowerPoint
serverSocket = socket(AF_INET, SOCK_DGRAM) #SocketAPI PowerPoint
serverSocket.bind((serverIP,serverPort)) #SocketAPI PowerPoint
print('The server is ready to recieve on port ' + str(serverPort)) #SocketAPI PowerPoint
i = 1
while True: #SocketAPI PowerPoint
	
	data, address = serverSocket.recvfrom(dataLen) #SocketAPI PowerPoint
	data2 = unpack("!I",data) #SocketAPI PowerPoint
	#print(data2) # made to test the pack and unpack method
	if ( randint(1,10) > 7 ):
		print("Message with sequence number "+ str(i)+ " dropped")
		i = i + 1
		continue
	else:
		print("Responding to ping request with sequence number " + str(i))
		i = i + 1
		serverSocket.sendto(pack("!I",2),address) #SocketAPI PowerPoint
	if (i > 10):
		i = 1
	else:
		continue
