import socket, threading
import subprocess
from threading import current_thread
import time
import mysql.connector

# This will retain the local variables within thread,
CurrentClient = threading.local()


def ConnectToMySQL (TableName, StrToMySQL) :
    tries = 10
    while tries > 0 :
        tries -= 1
        try : 
            connection = mysql.connector.connect(host='localhost', database='UCSDrobocar04_DataBase', user = 'server_process', password='team4ucsd')
        except mysql.connector.errors.ProgrammingError:
            if tries == 0:
                print ("Failed to connect even after retrying " + str(tries) + " times")
                break;    
            else :
                print ("retrying after 1 secs, Try Attempt:" + str(10-tries))
                time.sleep(1)
        else :
            break
    cursor = connection.cursor()
    cursor.execute('USE UCSDrobocar04_DataBase;')
    if StrToMySQL == 'Nothing' :
        print ("Nothing to add/overwrite to table")
    else :
        cursor.execute(StrToMySQL)
        connection.commit()    ## you need to send this to commit the current transaction. Since by default Connector/Python does not autocommit, it is important
                        ## to call this method after every transaction that modifies data for tables that use transactional storage engines.
    DescribeStr = 'SELECT * FROM ' + TableName + ';'
    cursor.execute(DescribeStr)
    record = cursor.fetchall()
    print(record)
    print("Done!! closing MySQL Connection")
    cursor.close()
    connection.close()

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
        data = self.csocket.recv(2048)
        msg = (data.decode()).rstrip()
        ClientName = msg[20:]
        ## for some reason, the client socket doesnt close properly unless it has received something from server..
        print("Client IpAddr:",CurrentClient.val,", Client Name:",ClientName)
        while True:
            msg = "Welcome! Would to like to initiate travel, please enter \'yes\' to continue; any other value to abort connection:"
            self.csocket.send(bytes(msg,'UTF-8'))
            data = self.csocket.recv(2048)
            msg = (data.decode()).rstrip()
            if  msg != 'yes':
                self.csocket.send(bytes(msg,'UTF-8'))
                break
            print("Received Yes, sending commands to reqeust for start dest")
            msg = 'Please Enter Start Destination in format Px (case sensitive), if incorrect format provided, will default to P1:'
            self.csocket.send(bytes(msg,'UTF-8'))
            data = self.csocket.recv(2048)
            msg = (data.decode()).rstrip()
            StartDestination = 'P1'
            print("thread:",CurrentClient.val,", Msg from client",msg)
            if msg == 'P1' or msg == 'P2' or msg == 'P3' :
                print("Valid entry, adding to DB:",msg)
                StartDestination = msg
            else :
                print("Invalid entry, added P1 to DB")
            print("Established Start Dest, sending commands to reqeust for end dest")
            msg = 'Entry ' + StartDestination + ' To be Added to db, please enter End Destination in format Px (case sensitive), in incorrect format, will default to P3:'
            self.csocket.send(bytes(msg,'UTF-8'))
            data = self.csocket.recv(2048)
            msg = (data.decode()).rstrip()
            EndDestination = 'P3'
            print("thread:",CurrentClient.val,", Msg from client",msg)
            if msg == 'P1' or msg == 'P2' or msg == 'P3' :
                print("Valid entry, adding to DB:",msg)
                EndDestination = msg
            else :
                print("Invalid entry, added P3 to DB")
            print("Entry added to mySQL database and sleep for 3 secs before sending message to client again")
            msg = "End Destination added as:" + EndDestination + " ,Thank you for using PTS! Have a good day"
            tableName = 'TransferRequest'
            strToMySQL = "REPLACE INTO TransferRequest VALUES (\'" + ClientName + "\',\'" + StartDestination + "\',\'" + EndDestination + "\');"
            print(strToMySQL)
            ConnectToMySQL (tableName, strToMySQL)
            time.sleep(3)
            self.csocket.send(bytes(msg,'UTF-8'))
        print("Client at", CurrentClient.val, "disconnected..")


print('Establishing test connection to see if DB is usable by server_process')


tableName = 'TransferRequest'
strToMySQL = 'Nothing'
ConnectToMySQL (tableName, strToMySQL)


print("Starting Server Socket Connection")

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

