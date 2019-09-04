import socket

Server_IP = (input("Enter the IP addr of Server to establish connection: ")).rstrip()
User_Name = (input("Enter your name to create new entry or update your account details for travel expenses: ")).rstrip()
#SERVER = "192.168.55.1"
SERVER = Server_IP
PORT = 11111
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER,PORT))
Msg_to_server = "This is from Client:" + User_Name
client.sendall(bytes(Msg_to_server, 'UTF-8'))
while True:
    in_data = client.recv(1024)
    out_data = (input(in_data.decode())).rstrip()
    client.sendall(bytes(out_data, 'UTF-8'))
    if out_data != 'yes':
        print("Terminating Connection as entered command is not yes")
        break
    in_data = client.recv(1024)
    out_data = (input(in_data.decode())).rstrip()
    client.sendall(bytes(out_data, 'UTF-8'))
    in_data = client.recv(1024)
    out_data = (input(in_data.decode())).rstrip()
    client.sendall(bytes(out_data, 'UTF-8'))
    in_data = client.recv(1024)
    print("From Server :", in_data.decode())
	
client.close()
