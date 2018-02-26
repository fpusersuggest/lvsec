#!/usr/bin/env python


aptdir='lvaptarchives'
import apt_pkg
import apt
from time import sleep
from os import uname
from os import path
from os import mkdir


def f_getpkgs(file):
    with apt_pkg.TagFile('/var/lib/dpkg/status') as tagfile:
        for section in tagfile:
            print(section['Package'])

def f_geturi():
    for p in cache:
        if p.is_installed:
            print p.candidate.uri

def f_getpkg(pkg):
    if not path.isdir(aptdir):
        mkdir(aptdir)
    p=apt.progress.text.AcquireProgress()
    c=apt.Cache()
    u=c[pkg].candidate.uri
    a=apt_pkg.Acquire(p)
    acq=apt_pkg.AcquireFile(a,uri=u,destdir=aptdir)
    a.run()

def f_getkernel():
    kv="linux-image-"+uname()[2]
    f_getpkg(kv)





def f_getlist():
    list=apt_pkg.SourceList()
    list.read_main_list()
    for a in list:
        print a
#
#def f_test():
#    p=apt.progress.text.AcquireProgress()
#    f=apt_pkg.Acquire(p)
#
#
f_getlist()

