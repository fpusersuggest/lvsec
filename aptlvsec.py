#!/usr/bin/env python

import apt_pkg
import apt

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
    print pkg
    pkg="linux-image-4.4.0-116-generic"
    p = apt.progress.text.AcquireProgress()
    c=apt.Cache()
    print c
    uri=c[pkg].candidate.uri
    print uri
    aqui=apt_pkg.Acquire(p)
    print aqui
    apt_pkg.AcquireFile(aqui,uri=uri)
    res=aqui.run()

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
