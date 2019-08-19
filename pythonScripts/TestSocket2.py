#!/usr/bin/env python3

import socket
import subprocess

proc = subprocess.Popen('ifconfig | grep "inet .* broadcast .*"',shell=True,stdout=subprocess.PIPE,)
output = str((proc.communicate()[0]).strip()).split(" ")[1]

HOST = output
PORT = 11111

print("Initiating Socket with IPAddr:",HOST," and PORT:",PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((HOST,PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by:',addr, " with conn:",conn)
        while True:
            data=conn.recv(1024)
            print("Data Received is : ",data)
            if not data:
                break
            print ("Sending Data to Client")
            conn.sendall(data)

