# Satyanveshi Security Scanner
Dynamic and basic security scanner with functionality of host discovery, port scanning, spidering and vulnerability scanning. Basic vulnerabilty scanning is still in progress.

![image](https://user-images.githubusercontent.com/75296055/144710871-92286c9d-8e71-4f53-98b8-69f75976a04d.png)

Current version available is 2021.3.1.

### Installation 
1. `git clone https://github.com/shaan453/Satyanveshi-Security-Scanner.git`
2. `cd satyanveshi-security-scanner`

### Usage
`python3 main.py <target> <modes>`

-Options
Usage: python3 main.py <option(s)> <target> <other-options(optional)>
    --portscan          Scan ports
       -sF:             Full scan. Scan 63000 ports.
       -sH:             Half scan. Scan 30000 ports.
       -sB:             Baby scan. Scan 1000 ports.
    --spider            Spider
    --hostdiscovery     Discover hosts
    --vulnscan (alpha)  Vulnerability Scan
