import requests
import re
import sys
import threading
import socket

def portscan(url):
	startingPort = 0
	endingPort = 0
	if sys.argv[3] == "-sF":
		endingPort = 30000
	if sys.argv[3] == "-sH":
		endingPort = 10000
	if sys.argv[3] == "-sB":
		endingPort = 1000
	scanning(url,startingPort,endingPort)

def scanning(url,startingPort,endingPort):
	for port in range(startingPort,endingPort+1):
		Thread = threading.Thread(target = scanPorts,args=(url,port,))
		Thread.start()

def scanPorts(url,port):
	con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	final = con.connect_ex((url,port))
	if final:
		pass
	else:
		portSet = "Port {} is open".format(port)
		print(portSet)
		if sys.argv[-2] == "-o":
			file = open(sys.argv[-1]+".txt","a")
			file.write(portSet+"\n")
			file.close()
		else:
			pass
	con.close()