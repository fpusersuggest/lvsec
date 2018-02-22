#!/usr/bin/env python

from tasklog import *
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
    c=apt.Cache()
    uri=c[pkg].candidate.uri
    aqui=apt_pkg.Acquire()
    apt_pkg.AcquireFile(aqui,uri=uri)
    aqui.run()





