import datetime
import pyfiglet

def design_banner():
    print(pyfiglet.figlet_format("Sec Scanner"))
    print("[*] Usage: python3 main.py <option(s)> <target> <other-options(optional)>")
    print('''    --portscan          Scan ports
       -sF:             Full scan. Scan 63000 ports.
       -sH:             Half scan. Scan 30000 ports.
       -sB:             Baby scan. Scan 1000 ports.
    --spider            Spider
    --hostdiscovery     Discover hosts
    --vulnscan (alpha)  Vulnerability Scan
    ''')

def banner():
    print("-"*70)
    print("Starting satyanveshi 2021.2.10 at ",datetime.datetime.now())
    print("-"*70)