#!/usr/bin/env python

import os, sqlite3
from tasklog import *
from uuid import uuid1
from datetime import datetime

#__name__="db"
v_file_db="dblvsec.db"
v_file_sch="dblvsec.sql"


def f_query(sql, data):
    with sqlite3.connect(v_file_db) as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA Foreign_Keys = ON")
        cursor.execute(sql, data)
        result = cursor.fetchall()
        db.commit()
        return result
        
    
def f_conn(file2):
    try:
        c=sqlite3.connect(file2)
    except:
        print("Error")


def f_create_db(file1):
    f_print("DB not found, I am going to create it")
    db=sqlite3.connect(v_file_db)
    cur=db.cursor()
    f=open(file1, "r")
    cur.executescript(f.read())
    db.commit()
    f_ok()

def f_create_dbfile():
    newuuid=uuid1()
    data=datetime.now()
    g=str(data.day)
    m=str(data.month)
    y=str(data.year)
    h=str(data.hour)
    mi=str(data.minute)
    s=str(data.second)
    desc=h+":"+mi+":"+s+"  "+g+"-"+m+"-"+y
    sql = """
    INSERT INTO {0}(desc,data,uuid,tipo,concluso) VALUES (?,?,?,?,?)
    """.format(table_name)
    f_query(sql,(desc,data,newuuid,tipo,concluso))
    


def main():
    f_ok()
    #m_conn = f_conn(v_file_db)
    #print "stampo m_conn "+str(m_conn)
    f_print("Try to connect to db")
    if os.path.isfile(v_file_db) is not True:
        f_fail()
        f_create_db(v_file_sch)
    else:
        m_conn=f_conn(v_file_db)
        f_ok()


if __name__ == '__main__':
    f_print("Let's start")
    main()


