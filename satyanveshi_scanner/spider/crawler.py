import requests
import re
import sys
import threading
import socket

def getRawData(urlContent):
    return re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(urlContent))

def getDomains(rawData):
    domains = []
    for i in range(len(rawData)):
        domains.append(rawData[i])
    return domains

def getInput():
    if sys.argv[1] == "--scan":
        url = "https://" + str(sys.argv[2])
        return url
    elif sys.argv[1] == "--portscan":
        host = socket.gethostbyname(str(sys.argv[2]))
        return host
    elif sys.argv[1] == "--hostdiscovery":
        host = str(sys.argv[2])
        return host
    else:
        return None

def getContent(url):
    getResult = requests.get(url)
    urlContent = getResult.content
    getResult.close()
    return urlContent

def setOutput(domains):
    f = open("spider-result.txt","a")
    for i in range(len(domains)):
        f.write(str(domains[i]) + "\n")
    f.close
    print("File saved in ", f.name)

def spidering(url):
    rawData = getRawData(getContent(url))
    parentDomains = getDomains(rawData)
    try:
        spider = threading.Thread(target=multitask, args=(parentDomains,url,))
        spider.start()
    except():
        print("Problem occured")
    except(KeyboardInterrupt):
        print("Stopping... Keyboard Interupt")
    print("File saved")
    sys.exit()

def multitask(parentDomains,url):
    for i in range(len(parentDomains)):
        rawDataChild = None
        domains = []
        rawDataChild = getRawData(getContent(parentDomains[i]))
        domains = getDomains(rawDataChild)
        for x in range(len(domains)):
            f = open("spider-result.txt","a")
            url = url[:-4].replace("https://", "")
            if url in str(domains[x]):
                f.write(str(domains[x]) + "\n")
            f.close() 