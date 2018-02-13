#Thomas Livshits
#tl263
#CS 356-002

#Client

import sys,time #SocketAPI PowerPoint
from socket import * #SocketAPI PowerPoint
from random import *
from time import sleep
from struct import * #SocketAPI PowerPoint
from functools import reduce # https://stackoverflow.com/questions/9039961/finding-the-average-of-a-list
argv = sys.argv #SocketAPI PowerPoint
host = argv[1] #SocketAPI PowerPoint
port = argv[2] #SocketAPI PowerPoint
count = 10
port = int(port) #SocketAPI PowerPoint
count = int(count) #SocketAPI PowerPoint
data = 1
i = 1
data2 = pack("!I",data) #SocketAPI PowerPoint

clientsocket = socket(AF_INET, SOCK_DGRAM) #SocketAPI PowerPoint
j = 0 
k = 0
times = [] #https://developers.google.com/edu/python/lists
while (i < 11):
	start_time = time.time()
	print("Pinging " + host+", " + str(port)) #SocketAPI PowerPoint
	clientsocket.sendto(data2,(host,port)) #SocketAPI PowerPoint
	#sleep(randint(1,10))
	clientsocket.settimeout(5) #https://stackoverflow.com/questions/3432102/python-socket-connection-timeout
	try: #https://stackoverflow.com/questions/3432102/python-socket-connection-timeout
		dataEcho, address = clientsocket.recvfrom(count) #SocketAPI PowerPoint
		data3 = unpack("!I",dataEcho) #SocketAPI PowerPoint
		#print(data3) #created to test if the unpack and pack method worked
		elapsed_time = time.time() - start_time
		elapsed_time = elapsed_time
		times.append(elapsed_time) #https://developers.google.com/edu/python/lists
		print("Ping message number " + str(i) + " RTT: " + str(elapsed_time) + " secs")
		i = i +1
		k = k + 1
	except: #https://stackoverflow.com/questions/3432102/python-socket-connection-timeout
		print("Ping message number " + str(i) + " timed out")
		i = i + 1
		j = j + 1
		continue
clientsocket.close() #SocketAPI PowerPoint
print("___________________________________________________")
times.sort() #https://developers.google.com/edu/python/lists
lmax = len(times)-1
avg = reduce(lambda x, y: x + y, times) / len(times) # https://stackoverflow.com/questions/9039961/finding-the-average-of-a-list
print("Packets sent : " + str(k+j))
print("Packets received : " + str(k))
print("Packets lost : " + str(j))
print("% of Packets lost : " + str(j/(j+k)))
print("Min RTT : " + str(times[0]))
print("Max RTT : " + str(times[lmax]))
print("Avg RTT : " + str(avg))
print("___________________________________________________")

