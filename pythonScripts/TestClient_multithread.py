import socket

Server_IP = (input("Enter the IP addr of Server to establish connection: ")).rstrip()
#SERVER = "192.168.0.104"
SERVER = Server_IP
PORT = 11111
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER,PORT))
client.sendall(bytes("This is from Client", 'UTF-8'))
while True:
    in_data = client.recv(1024)
    print("From Server :", in_data.decode())
    out_data = (input("Enter the command you wish to send, enter \'bye\' to terminate connection: ")).rstrip()
    client.sendall(bytes(out_data, 'UTF-8'))
    if out_data =='bye':
        print("Terminating Connection")
        break
client.close()