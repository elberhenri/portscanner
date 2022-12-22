#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])#Translate hostname to IPv4
else:

    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")

#Add a pretty banner
print("-" * 50)
print("Scanning target:" + target)
print("TIme started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #"s.connect_ex, SO if a port is open, the error result returns zero (ok), If a port is closed it returns a one (nok)"
        if result == 0:
            print(f"Port {port} is open")
        s.close() #"we're gonna close this, then we're gonna go back to the loop"

except KeyboardInterrupt: #"control c to interrupt the program"
    print("\nExiting Program.")
    sys.exit()
except socket.gaierror: #"ex: python3 scanner.py kjasksjak"
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error: #"its just not online, it doesn't talk back to us"
    print("Could not connect to server.")
    sys.exit()
    