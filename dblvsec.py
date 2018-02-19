#!/usr/bin/env python

import os, sqlite3
from tasklog import *
#__name__="db"
v_file_db="dblvsec.db"
v_file_sch="dblvsec.sql"


def f_conn(file):
	"""Crea una connessione al database"""
	try:
		f_print("Connessione al db")
		c=sqlite3.connect(file)
		#print "stampo c = "+str(c)
                if c is True:
                    f_ok()
                else:
                    f_fail()
	except:
		f_fail()


def create_table(conn, create_table_sql):
	"""Crea una tabella"""
	try:
		c=conn.cursor()
		c.execute(create_table_sql)
	except Error as e:
		print(e)


def main():
	#m_conn = f_conn(v_file_db)
	#print "stampo m_conn "+str(m_conn)
        f_print("Try to connect to db")
	if os.path.isfile(v_file_db) is not True:
                f_fail()
                f_print("Database not found, I create it")
	        m_conn_create = f_conn(v_file_db)
		m_schema=open(v_file_sch,"r").read()
		m_cursore_create=m_conn_create.cursor()
		m_ins_create=map(lambda x: x.lstrip().replace("\n"," "),m_schema.split(";"))
		map(m_cursore_create.execute, m_ins)
                if m_conn_create.commit() is True:
                    f_ok()
                else:
                    f_fail()
	else:
		m_conn=f_conn(v_file_db)
                if m_conn is True: 





if __name__ == '__main__':
    f_print("Let's start")
    main()







