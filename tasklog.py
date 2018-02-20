#!/usr/bin/env python

from __future__ import print_function
import os

v_col=40
v_inzio='\033[1;32m'
v_ok='[\033[1;32m  OK  \033[1;m]'
v_fa='[\033[1;31m FAIL \033[1;m]'
v_fine='\033[1;m'

def f_ok():
	"""Task log pretty output"""
        print(v_ok)
		 
def f_print(t):
    n="."*(50-len(t))+" " 
    print("[-] "+t+n, end='')

def f_fail():
	"""Task log pretty output"""
        print(v_fa)


