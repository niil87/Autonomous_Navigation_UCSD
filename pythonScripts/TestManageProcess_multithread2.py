import mysql.connector
import time

def ConnectToMySQL_Manage (TableName, StrToMySQL) :
    tries = 10
    while tries > 0 :
        tries -= 1
        try : 
            connection = mysql.connector.connect(host='localhost', database='UCSDrobocar04_TransferRequest', user = 'manage_process', password='team4ucsd')
        except mysql.connector.errors.ProgrammingError:
            if tries == 0:
                print ("Failed to connect even after retrying " + str(tries) + " times")
                break;    
            else :
                print ("retrying after 10 ms, Try Attempt:" + str(10-tries))
                time.sleep(0.01)
        else :
            break
    cursor = connection.cursor()
    cursor.execute('USE UCSDrobocar04_TransferRequest;')
    cursor.execute(StrToMySQL)
    record = "Nothing"
    if 'REPLACE' in StrToMySQL : 
        connection.commit()
        DescribeStr = 'SELECT * FROM ' + TableName + ';'
        cursor.execute(DescribeStr)
        record = cursor.fetchall()
    else : 
        record = cursor.fetchall()
    print("Done!! closing MySQL Connection")
    cursor.close()
    connection.close()
    return record


print('Establishing test connection to see if DB is usable by server_process')

tableName = 'TransferRequest'
strToMySQL = 'SELECT * FROM TransferRequest;'
print(strToMySQL)
retn = ConnectToMySQL_Manage (tableName, strToMySQL)
print (retn)


command = (input("Please Enter Start/End Destination in Px form that you would like to find: ")).rstrip()
strToMySQL = "SELECT * FROM TransferRequest WHERE (StartLocation = \'" + command + "\' OR EndLocation = \'" + command + "\');"
print(strToMySQL)
retn = ConnectToMySQL_Manage (tableName, strToMySQL)
print ("SQL Query returned: " + str(retn))
if retn == [] : 
    print ("No need to stop")
else :
    print(retn)
    print ("Location found, please stop")


if retn is not []:
    print ("Erasing entry")
    for entry in retn :
        if entry[1] == command :
            newStartDest = 'NULL'
        else :
            if entry[1] is not None :
                newStartDest = "\'" + entry[1] + "\'"
            else : 
                newStartDest = 'NULL'

        if entry[2] == command and entry[1] is None:
            newEndDest = 'NULL'
        else :
            newEndDest =  "\'" + entry[2] + "\'"

        print("New Tuple:" + entry[0] + ' ' + newStartDest + ' ' + newEndDest + ' ')
        strToMySQL = "REPLACE INTO TransferRequest VALUES (\'" + entry[0] + "\'," + newStartDest + "," + newEndDest + ");"
        print (strToMySQL)
        retn = ConnectToMySQL_Manage (tableName, strToMySQL)

