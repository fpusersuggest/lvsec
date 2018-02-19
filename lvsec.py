#!/usr/bin/python

import apt, sys, progressbar, argparse, argcomplete
import db


db_name = 'lvsec.db'

pArgs=argparse.ArgumentParser(
	description='lvsec, check system security on Ubuntu or Fedora distro',
	epilog='Software to check ubuntu installed packages')
pArgs.add_argument('--root-apt', 
	help='Indica la root dove si trava la cache di APT',
	default='/')
pArgs.add_argument('--save-dir',
	help='Indica la cartella dove salvare di pacchetti .deb')
args = pArgs.parse_args()
status=apt.Cache(rootdir=fileStatus)
db_is_new = not os.path.exists(db_filename)
conn = sqlite3.connect(db_filename)

if db_is_new:
    print 'Occorre creare lo schema'
else:
    print 'Il database esiste, si suppone che esista anche lo schema.'

conn.close()
