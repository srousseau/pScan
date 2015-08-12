# Scott Rousseau
# Basic Port Scanner

import socket, subprocess, sys
from datetime import datetime

#RemoteServerIP = argv[1]

# Ask for input
remoteServer    = raw_input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

rangeStart = raw_input("Enter the starting port range: ")
rangeEnd = raw_input("Enter the ending port range: ")

rangeStart = int(rangeStart)
rangeEnd = int(rangeEnd)

print "*" * 80
print "[*] Please wait, scanning remote host:" + remoteServer + " IP:" + str(remoteServerIP)
print "*" * 80

t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)

# We also put in some error handling for catching errors

try:
    for port in range(rangeStart,rangeEnd):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}: \t Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "[*] User interuppted scan"
    sys.exit()

except socket.gaierror:
    print '[*] Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "[*] Couldn't connect to server"
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print '[*] Scanning Completed in: ', total

