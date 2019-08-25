import mysql.connector
connection = mysql.connector.connect(host='localhost', database='test1', user = 'nikhil', password='team4ucsd')
cursor = connection.cursor()
cursor.execute('SHOW DATABASES;')
record = cursor.fetchall()
print(record)
print("Done!!")
