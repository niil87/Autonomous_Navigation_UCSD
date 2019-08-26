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

## no need to protection for this if LOCK TABLES is used.. as this will put the process on hold instead of crashing; until UNLOCK IS CALLED
cursor.execute('SELECT * FROM PriceList;')
record = cursor.fetchall()
print(record)
cursor.execute('INSERT INTO PriceList VALUES (\'P1\',1.0)')
connection.commit()
a = input("Enter anything to continue")
cursor.close()
connection.close()
print("Done!!")
