#!/usr/bin/env python

import os, sqlite3
from tasklog import *
from uuid import uuid1

#__name__="db"
v_file_db="dblvsec.db"
v_file_sch="dblvsec.sql"


def f_conn(file2):
    try:
        c=sqlite3.connect(file2)
    except:
        print("Error")


def f_create_db(file1):
    f_print("DB not found, I am going to create it")
    conn=sqlite3.connect(v_file_db)
    cur=conn.cursor()
    f=open(file1, "r")
    cur.executescript(f.read())
    conn.commit()
    f_ok()


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


