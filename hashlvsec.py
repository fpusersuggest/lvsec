#!/usr/bin/env python

from os import path
from hashlib import sha256,md5
import tasklog

mbrdir="./storedata/"

def f_gethash(filename):
    hashmd5=md5()
    hash256=sha256()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hashmd5.update(chunk)
            hash256.update(chunk)
    m5=hashmd5.hexdigest()
    s256=hash256.hexdigest()
    print "Hash sha256 ==> "+s256
    print "Hash md5 =====> "+m5
    return m5,s256

def f_gethashmbr(disk):
    tasklog.f_print("Checking if storagedata directory exist.")
    if not path.exists(mbrdir):
        tasklog.f_fail()
        from os import mkdir
        tasklog.f_print("Directory storagedata not found, creating it")
        mkdir(mbrdir)
        tasklog.f_ok()
    else:
        tasklog.f_ok()
    d=str(disk).split('/')[2]
    mbrout=mbrdir+"mbr-"+d
    with open(disk) as r, open(mbrout,'w') as w:
        tasklog.f_print("Try to open "+disk+" to save mbr on "+mbrout) 
        hash5=md5()
        hash256=sha256()
        mbr=r.read(512)
        hash5.update(mbr)
        hash256.update(mbr)
        mbrw=w.write(mbr)
    if not mbrw:
        tasklog.f_ok()
    else:
        tasklog.f_fail()
    tasklog.f_print("Calculating mbr hashes")
    m5=hash5.hexdigest()
    s256=hash256.hexdigest()
    if m5 and s256:
        tasklog.f_ok()
    else:
        tasklog.f_fail()
    print "Hash MBR md5 =====> "+m5
    print "Hash MBR sha256 ==> "+s256
    return m5,s256

