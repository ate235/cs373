#!/usr/bin/env python

import types

class A (object) :
    def f (self) :
        pass


print type(A.f) is types.MethodType

print "Done."
