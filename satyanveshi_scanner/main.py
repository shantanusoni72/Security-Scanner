import requests
import re
import sys
import threading
from spider.crawler import *
from portscan.portscans import *
from hostdiscovery.discovery import *
from res.design import *
from vulnerability.bugscanner import *


if __name__ == "__main__":
    url = getInput()
    if sys.argv[1] == "--spider":
        banner()
        spidering(url)
    elif sys.argv[1] == "--portscan":
        banner()
        portscan(url)
    elif sys.argv[1] == "--hostdiscovery":
        banner()
        hostdiscovery(url)
    elif sys.argv[1] == "--vulnscan":
        banner()
        vulnscan()
    else:
        design_banner()