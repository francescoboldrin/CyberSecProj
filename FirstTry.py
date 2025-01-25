'''
Author: francesco boldrin francesco.boldrin@studenti.unitn.it
Date: 2024-09-03 13:17:13
LastEditors: francesco boldrin francesco.boldrin@studenti.unitn.it
LastEditTime: 2024-09-04 12:07:45
FilePath: FirstTry.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
'''

import numpy as np
import socket
import threading

TARGET_IP = "89.46.108.51"

START_PORT = 1
END_PORT = 1024

def check_connection(ip):
    try:
        socket.gethostbyaddr(ip)
        print(f"Connection to {ip} successful")
        return True
    except:
        return False
def find_open_ports(ip, start_port, end_port):
    print (f"Scanning {ip} from {start_port} to {end_port}")
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                print(f"Trying port {port}")
                s.settimeout(0.1)
                s.connect((ip, port))
                open_ports.append(port)
                if port % 100 == 0:
                    print(f"Port {port} is open")
                    break
        except:
            pass
    return open_ports

def communicate(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        s.sendall(b"Hello, world")
        data = s.recv(1024)
        print(f"Received: {data.decode()}")
        
def main():
    if not check_connection(TARGET_IP):
        print("Connection failed")
        return
    open_ports = find_open_ports(TARGET_IP, START_PORT, END_PORT)
    print(f"Open ports: {open_ports}")
    for port in open_ports:
        threading.Thread(target=communicate, args=(TARGET_IP, port)).start()

if __name__ == "__main__":
    main()