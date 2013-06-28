#!/usr/bin/env python

"""
CS373: Quiz #8 (10 pts)
"""

""" ----------------------------------------------------------------------
1. What is the output of the following?
   (9 pts)

0 0
0 0
0 1
"""

class A (object) :
    def __init__ (self) :
        self.i = 0

    def __call__ (self) :
        v = self.i
        self.i += 1
        return v

print A()(),
print A()()

x = A
print x()(),
print x()()

y = x()
print y(),
print y()
