import sqlite3
from os.path import exists
from unittest import result

def creation():
    conn=sqlite3.connect("programe.db")
    c=conn.cursor()
    c.execute("CREATE table users(nom varchar(50) PRIMARY KEY,secnom varchar(50),pass varchar(50));")
    conn.commit()
    conn.close()
def connection():
    if(not exists("programe.db")):
        
        creation()
    conn=sqlite3.connect("programe.db")
    return conn
def searchusers(nom,passord):
    conn=connection()
    sql=f"select * from users where nom='{nom}' and pass='{passord}'"
    c=conn.cursor()
    c.execute(sql)
    x=c.fetchmany()
    conn.close()
    return x
def serachname(nom):
    conn=connection()
    sql=f"select * from users where nom='{nom}'"
    c=conn.cursor()
    c.execute(sql)
    x=c.fetchmany()
    conn.close()
    return len(x)==1
def login(name,password):
    if(len(searchusers(name,password))==0):
        return False
    else:
        return True
def adduser(nom,second,passw):
    conn=connection()
    sql=f"insert into users values('{nom}','{second}','{passw}')"
    c=conn.cursor()
    c.execute(sql)
    conn.commit()
    conn.close()
def getinformation(nom):
    conn=connection()
    sql=f"select secnom,pass from users where nom='{nom}'"
    c=conn.cursor()
    c.execute(sql)
    x=c.fetchmany()
    conn.close()
    return x[0]
