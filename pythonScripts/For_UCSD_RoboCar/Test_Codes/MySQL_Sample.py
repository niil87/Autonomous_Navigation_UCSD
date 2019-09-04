import mysql.connector
import time

tries = 10
while tries > 0 :
    tries = tries - 1
    try : 
        connection = mysql.connector.connect(host='localhost', database='UCSDrobocar04_DataBase', user = 'server_process', password='team4ucsd')
    except mysql.connector.errors.ProgrammingError:
        if tries == 0:
            print ("Failed to connect even after retrying " + str(tries) + " times")
            break;    
        else :
            print ("retrying after 1 secs")
            time.sleep(1)
    else:
        break
cursor = connection.cursor()
cursor.execute('DESCRIBE PriceList;')
record = cursor.fetchall()
print(record)
cursor.execute('LOCK TABLES PriceList WRITE;')
connection.commit()
a = input("Enter anything to continue")
cursor.execute('UNLOCK TABLES;')
connection.commit()
cursor.close()
connection.close()
print("Done!!")
