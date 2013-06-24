#!/usr/bin/env python

"""
CS373: Quiz #6 (10 pts)
"""

""" ----------------------------------------------------------------------
1. What is the output of the following program?
   (4 pts)

[[2, 5], [3, 5], [4, 5]]
[(2,), (3,), (4,)]
"""

a = [[2], [3], [4]]
for v in a :
    v += (5,)
print a

a = [(2,), (3,), (4,)]
for v in a :
    v += (5,)
print a
print

""" ----------------------------------------------------------------------
2. What is the output of the following program?
   (5 pts)

m1 m2 f1 m3 f1 m4
"""

def f () :
    print "f1",
    yield f()
    print "f2",

print "m1",
x = f()
print "m2",
y = x.next()
print "m3",
z = y.next()
print "m4"
