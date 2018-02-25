#!/usr/bin/env python

import apt_pkg
import apt
from time import sleep
from os import uname

def f_getpkgs(file):
    with apt_pkg.TagFile('/var/lib/dpkg/status') as tagfile:
        for section in tagfile:
            print(section['Package'])

def f_geturi():
    for p in cache:
        if p.is_installed:
            print p.candidate.uri

def f_getpkg(pkg):
    pkg="linux-image-4.4.0-116-generic"
    p=apt.progress.text.AcquireProgress()
    c=apt.Cache()
    u=c[pkg].candidate.uri
    a=apt_pkg.Acquire(p)
    apt_pkg.AcquireFile(a,uri=u)
    a.run()



f_getpkg("linux-image-4.4.0-116-generic")



#def f_getlist():
#    list=apt_pkg.SourceList()
#    list.read_main_list()
#    for a in list:
#        print a
#
#def f_test():
#    p=apt.progress.text.AcquireProgress()
#    f=apt_pkg.Acquire(p)
#
#
