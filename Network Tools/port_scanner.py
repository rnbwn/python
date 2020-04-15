"""
 ***************************************************************************
 * Scanner that checks all open ports on any website/ip that exists.       *
 * Works better in the python IDLE state rather than command prompt.       *
 *                                                                         *
 *                                                                         *
 * developed by Stefan Batricevic                                          *
 * https://github.com/rnbwn                                                *
 ***************************************************************************
"""
import socket, sys
from threading import Thread
import threading
import time

threads = []
timeout = 0.5
ports = []

try:
   host = input("Enter Target Host Address: ")
   hostIP = socket.gethostbyname(host)
   startPort = int(input("Enter Starting Port to Scan: "))
   endPort = int(input("Enter Ending Port to Scan: "))

except KeyboardInterrupt:
    print("\n\n[*]User requested an interrupt[*]")
    sys.exit()

except socket.gaierror:
    print("\n\n[*]Hostname unresolvable[*]")
    sys.exit()

except socket.error:
    print("\n\n[*]Unable to connect to target[*]")
    sys.exit()


print ("Scanning Target: ", hostIP)
print("Scanning...")

def scanner(port):
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   socket.setdefaulttimeout(timeout)
   result = sock.connect_ex((hostIP, port))
   if result == 0:
      ports.append(port)
   sock.close()

for i in range(startPort, endPort+1):
   thread = Thread(target=scanner, args=(i,))
   while threading.active_count()> 500:
      time.sleep(1)
   thread.start()

print("Scanning completed!")
print("All open ports: ", ports)
