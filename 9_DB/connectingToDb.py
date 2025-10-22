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
    
mycursor.execute("create database if not exists indigo")
# whenever you change something in database write conn.commit()
conn.commit()


mycursor.execute("select * from olymp.food")
data=mycursor.fetchall()
print(data)