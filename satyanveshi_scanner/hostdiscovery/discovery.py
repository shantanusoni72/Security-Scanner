import requests
import re
import sys
import threading
import socket

def hostdiscovery(url):
    hostSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    for i in range(255):
        ip = str(url) + "." + str(i)
        connection = hostSocket.connect_ex((ip,7))
        if bool(connection):
            print("Host alive ",ip)
            if sys.argv[-2] == "-o":
                file = open(sys.argv[-1]+".txt","a")
                file.write(ip+"\n")
                file.close()
            else:
                pass
            connection.close()
        else:
            pass