#!/usr/bin/env python

"""
CS373: Quiz #21 (10 pts)
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following program?
    (9 pts)

A.A() A.A() False
A.A() True
True
"""

def Decorator (c) :
    x = c()
    return lambda : x

class A (object) :
    def __init__ (self) :
        print "A.A()",

print A() is A()

A = Decorator(A)
print A() is A()

A = Decorator(A)
print A() is A()
