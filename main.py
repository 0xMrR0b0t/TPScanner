import socket
import sys
from queue import Queue
import threading
from datetime import datetime
import os

def clear():
 
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')
clear()
    
print('''
      
$$$$$$$\                       $$\                                                                      
$$  __$$\                      $$ |                                                                     
$$ |  $$ | $$$$$$\   $$$$$$\ $$$$$$\          $$$$$$$\  $$$$$$$\ $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\ 
$$$$$$$  |$$  __$$\ $$  __$$\\_$$  _|        $$  _____|$$  _____|\____$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$  ____/ $$ /  $$ |$$ |  \__| $$ |          \$$$$$$\  $$ /      $$$$$$$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |      $$ |  $$ |$$ |       $$ |$$\        \____$$\ $$ |     $$  __$$ |$$ |  $$ |$$   ____|$$ |       
$$ |      \$$$$$$  |$$ |       \$$$$  |      $$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |\$$$$$$$\ $$ |      
\__|       \______/ \__|        \____/       \_______/  \_______|\_______|\__|  \__| \_______|\__|
|                                                                                                |
|--------------------------------------------Coded by Mohit--------------------------------------|''')

print("Github: https://github.com/0xMrR0b0t/tcp_port_scanner")


host = socket.gethostbyname(input("Enter Your ip/domain: "))

normalPortStart = 1
normalPortEnd = 1024
allPort = 1
allPortEnd = 65535
customPortStart = 0
customPortEnd = 0

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Select your scan type: ")
print("[+] Select 1 for normal port scaning")
print("[+] Select 2 for all port scaning")
print("[+] Select 3 for custom port scaning")
print("[+] Select 4 for exit \n")

mode = int(input("[+] Select any option: "))
print()

if mode == 3:
    customPortStart = int(input("[+] Enter starting port number: "))
    customPortEnd = int(input("[+] Enter ending port number: "))

print("-"*50)
print(f"Target IP: {host}")
print("Scanning started at:" + str(datetime.now()))
print("-"*50)
def scan(port):
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((host, port))
    if result == 0:
       print("port open", port)
    s.close()

# def thread(startingPort, endingPort):
#      for i in range(startingPort, endingPort + 1):
#         t = threading.Thread(target=scan, args=(i,))
#         t.start()
queue = Queue()
def get_ports(mode):
    if mode == 1:
        print("\n[+] scaning..\n")
        for port in range(normalPortStart, normalPortEnd):
            queue.put(port)
    elif mode == 2:
        print("\n[+] scaning..\n")
        for port in range(allPort, allPortEnd):
            queue.put(port)
    elif mode == 3:
        print("\n[+] scaning..\n")
        for port in range(customPortStart, customPortEnd):
            queue.put(port)
    elif mode == 4:
        print("[-] Exiting...")
        sys.exit()

open_ports = [] 
def worker():
    while not queue.empty():
        port = queue.get()
        if scan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)

def run_scanner(threads, mode):

    get_ports(mode)

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

run_scanner(1021, mode)
print(f"Scanning compleate in: {current_time}")

