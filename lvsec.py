#!/usr/bin/python


import apt, sys, progressbar, argparse, argcomplete

pArgs=argparse.ArgumentParser(description='lvsec, check system security on Ubuntu or Fedora distro',epilog='Software to check ubuntu installed packages')
pArgs.add_argument('--root-apt', help='Indica la root dove si trava la cache di APT',default='/')
pArgs.add_argument('--save-dir',help='Indica la cartella dove salvare di pacchetti .deb')
args = pArgs.parse_args()

status=apt.Cache(rootdir=fileStatus)

