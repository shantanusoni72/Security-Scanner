import requests
import re
import sys
import threading
from spider.crawler import *
from portscan.portscans import *
from hostdiscovery.discovery import *
from res.design import *


if __name__ == "__main__":
    url = getInput()
    if sys.argv[1] == "--scan":
        banner()
        spidering(url)
    elif sys.argv[1] == "--portscan":
        banner()
        portscan(url)
    elif sys.argv[1] == "--hostdiscovery":
        banner()
        hostdiscovery(url)
    else:
        print("[*] Invalid option")