import time
import mysql.connector


def ConnectToMySQL (TableName, StrToMySQL) :
    tries = 10
    DataBase = 'UCSDrobocar04_' + TableName
    while tries > 0 :
        tries -= 1
        try : 
            connection = mysql.connector.connect(host=HOST, database=DataBase, user = 'control_process', password='team4ucsd')
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
    cursor.execute('USE ' + DataBase + ';')
    if StrToMySQL == 'Nothing' :
        print ("Nothing to add/overwrite to table")
    else :
        cursor.execute(StrToMySQL)
        connection.commit()    ## you need to send this to commit the current transaction. Since by default Connector/Python 
                               ## does not autocommit, it is important to call this method after every transaction that modifies 
                               ## data for tables that use transactional storage engines.
    DescribeStr = 'SELECT * FROM ' + TableName + ';'
    cursor.execute(DescribeStr)
    record = cursor.fetchall()
    print("Done!! closing MySQL Connection")
    cursor.close()
    connection.close()
    return record


tableName = 'VehicleMode'

command = (input("Enter what you would like to do, Display[D]/Normal[N]/School[S]: ")).rstrip()
if command == "D" : 
    strToMySQL = 'Nothing'
elif command == "N" :
    strToMySQL = "UPDATE VehicleMode SET Active='N' WHERE Modetype = 'School Bus';"
elif command == "S" :
    strToMySQL = "UPDATE VehicleMode SET Active='Y' WHERE Modetype = 'School Bus';"

HOST = 'localhost'   # mysql is set to localhost 
retn = ConnectToMySQL (tableName, strToMySQL)
print(retn)


