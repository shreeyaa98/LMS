import sqlite3
from tkinter import *

conn=sqlite3.connect('Emp.db')
cur=conn.cursor()
cur.execute("CREATE TABLE Emp (eid integer PRIMARY KEY,name text,salary integer NOT NULL,Dno integer)")
conn.commit()
cur.execute("INSERT INTO Emp VALUES (1,'Tenzu',1000,5)")
conn.commit()
cur.execute(SELECT * FROM Emp)
rows=cur.fetchall()
print(rows)
cur.close()