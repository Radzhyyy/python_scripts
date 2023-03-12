#Importing modules that will help the code run: 
import sys
import socket
import pyfiglet

#ASCII Banner
ascii_banner = pyfiglet.figlet_format("TryHackMe \n Python 4 Pentesters \nPort Scanner")
print(ascii_banner)


#target IP
ip = '10.10.249.238' 

#An empty “open_ports” array that will be populated later with the detected open ports:
open_ports =[] 

#port range to scan 
ports = range(1, 65535)


#Tries to connect to the port:
def probe_port(ip, port, result = 1): 
  try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout(0.5) 
    r = sock.connect_ex((ip, port))   
    if r == 0: 
      result = r 
    sock.close() 
  except Exception as e: 
    pass 
  return result

#for loop that iterates through the specified port list:
for port in ports: 
    sys.stdout.flush() 
    response = probe_port(ip, port) 
    if response == 0: 
        open_ports.append(port) 
    

if open_ports: 
  print ("Open Ports are: ") 
  print (sorted(open_ports)) 
else: 
  print ("Looks like no ports are open :(")


