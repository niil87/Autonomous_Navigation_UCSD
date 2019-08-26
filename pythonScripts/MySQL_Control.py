import mysql.connector
import time

tries = 10
while tries > 0 :
    tries = tries - 1
    try : 
        connection = mysql.connector.connect(host='localhost', database='UCSDrobocar04_DataBase', user = 'control_process', password='team4ucsd')
    except mysql.connector.errors.ProgrammingError:
        if tries == 0:
            print ("Failed to connect even after retrying " + str(tries) + " times")
            break;    
        else :
            print ("retrying after 1 secs, initial connection")
            time.sleep(1)
    else:
        break

cursor = connection.cursor()

tries = 10
while tries > 0 :
    tries = tries - 1
    try : 
        cursor.execute('SELECT * FROM PriceList;')
    except mysql.connector.errors.ProgrammingError:
        if tries == 0:
            print ("Failed to connect even after retrying " + str(tries) + " times")
            break;    
        else :
            print ("retrying after 1 secs")
            time.sleep(1)
    else:
        break
record = cursor.fetchall()
print(record)
cursor.execute('INSERT INTO PriceList VALUES (\'P1\',1.0)')
connection.commit()
a = input("Enter anything to continue")
cursor.close()
connection.close()
print("Done!!")
