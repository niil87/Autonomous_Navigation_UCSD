import mysql.connector
import time

def ConnectToMySQL_Manage (TableName, StrToMySQL) :
    tries = 10
    DataBase = 'UCSDrobocar04_' + TableName
    while tries > 0 :
        tries -= 1
        try : 
            connection = mysql.connector.connect(host='localhost', database=DataBase, user = 'manage_process', password='team4ucsd')
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
    cursor.execute('USE ' + DataBase+ ';')
    cursor.execute(StrToMySQL)
    record = "Nothing"
    if 'REPLACE' in StrToMySQL : 
        connection.commit()
        DescribeStr = 'SELECT * FROM ' + TableName + ';'
        cursor.execute(DescribeStr)
        record = cursor.fetchall()
    else : 
        record = cursor.fetchall()
    #print("Done!! closing MySQL Connection")
    cursor.close()
    connection.close()
    return record

def CheckLocation(location) :

    tableName = 'VehicleMode'
    strToMySQL = "SELECT Active FROM VehicleMode WHERE ModeType = \'School Bus\';"
    retn = ConnectToMySQL_Manage (tableName, strToMySQL)
    msg = "No msg"
    print(retn)
    if 'Y' in retn[0][0] :
        print ("Stop at all stops")
        msg = True
        return msg

    tableName = 'TransferRequest'
    strToMySQL = "SELECT * FROM TransferRequest WHERE (StartLocation = \'" + location + "\' OR (StartLocation IS NULL AND EndLocation = \'" + location + "\'));"
    #print(strToMySQL)
    retn = ConnectToMySQL_Manage (tableName, strToMySQL)

    #print ("SQL Query returned: " + str(retn))
    if retn == [] :
        msg = False
    else :
        #print(retn)
        msg = True
    return msg

def RemoveLocation(location) :

    tableName = 'TransferRequest'
    strToMySQL = "SELECT * FROM TransferRequest WHERE (StartLocation = \'" + location + "\' OR (StartLocation IS NULL AND EndLocation = \'" + location + "\'));"
    retn = ConnectToMySQL_Manage (tableName, strToMySQL)

    if retn == []:
        print ("Nothing to remove in database")
    else :
        print ("Erasing entry")
        for entry in retn :
            if entry[1] == location :
                newStartDest = 'NULL'
            else :
                if entry[1] is not None :
                    newStartDest = "\'" + entry[1] + "\'"
                else : 
                    newStartDest = 'NULL'

            if entry[2] == location and entry[1] is None:
                newEndDest = 'NULL'
            else :
                newEndDest =  "\'" + entry[2] + "\'"

            #print("New Tuple:" + entry[0] + ' ' + newStartDest + ' ' + newEndDest + ' ')
            strToMySQL = "REPLACE INTO TransferRequest VALUES (\'" + entry[0] + "\'," + newStartDest + "," + newEndDest + ");"
            #print (strToMySQL)
            retn = ConnectToMySQL_Manage (tableName, strToMySQL)


Mymsg = CheckLocation('R')
if Mymsg is True :
    print ("Stop")
else :
    print ("Dont Stop")

RemoveLocation('R')

