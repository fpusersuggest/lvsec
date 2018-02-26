#!/usr/bin/env python

from hashlib import sha256,md5


def f_gethash(filename):
    hash256=sha256()
    hashmd5=md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hashmd5.update(chunk)
            hash256.update(chunk)
    s256=hash256.hexdigest()
    m5=hashmd5.hexdigest()
    print "Hash sha256 ==> "+s256
    print "Hash md5 =====> "+m5
    return s256,m5


def f_gethashmbr():

