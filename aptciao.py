#!/usr/bin/env python

import apt_pkg
import apt


pkg="linux-image-4.4.0-116-generic"
c=apt.Cache()
u=c[pkg].candidate.uri
p=apt.progress.text.AcquireProgress()
a=apt_pkg.Acquire(p)
apt_pkg.AcquireFile(a,uri=u)
a.run()

