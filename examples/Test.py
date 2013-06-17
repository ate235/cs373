#!/usr/bin/env python

def p (s) :
    print s
    return 0

def f () :
    [p(v) for v in [2, 3, 4]]

print "Test.py"
print

f()

print "Done."
