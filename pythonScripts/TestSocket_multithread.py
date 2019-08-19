import socket, threading
import subprocess
from threading import current_thread

# This will retain the local variables within thread,
CurrentClient = threading.local()

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New Connection Added:", clientAddress)
    def run(self) :
        print("Connection from :", clientAddress)

        # This will create new attribute 'val' and assign clientAddress to it.
        # Note this is local variable and hence self life is still thread life
        CurrentClient.val = clientAddress 
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            ## for some reason, the client socket doesnt close properly unless it has received something from server..
            print("thread:",CurrentClient.val,", Msg from client",msg)
            self.csocket.send(bytes(msg,'UTF-8'))
            if  msg == 'bye' :
                break
        print("Client at", CurrentClient.val, "disconnected..")

proc = subprocess.Popen('ifconfig | grep "inet .* broadcast .*"',shell=True,stdout=subprocess.PIPE,)
output = str((proc.communicate()[0]).strip()).split(" ")[1]

HOST = output
PORT = 11111

print("Initiating Socket with IPAddr:",HOST," and PORT:",PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()

