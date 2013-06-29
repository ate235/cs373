#!/usr/bin/env python

# ------------
# Functions.py
# ------------

import sys

print "Test.py"

def f (r) :
    for s in r :
        print s,

x = open("Test.py")
f(x)
f(sys.stdin)

print "Done."
