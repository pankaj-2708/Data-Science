import mysql.connector

try:
    conn=mysql.connector.connect(
                                 host='127.0.0.1',
                                 user='root',
                                 password=""
                                 )
    mycursor=conn.cursor()
except Exception as E:
    print('Not connected',E)