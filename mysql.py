import mysql.connector

conn=mysql.connector.connect(host='localhost',database='sys',user='root')
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Emp (eid integer PRIMARY KEY,name text,salary integer NOT NULL,Dno integer)")
conn.commit()
cursor.execute("Insert into emp values (1,'prats',1000,6)")
conn.commit()
cursor.execute("SELECT * FROM Emp")
rows=cursor.fetchall()
print(rows)