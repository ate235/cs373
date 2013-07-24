#!/usr/bin/env python

"""
CS373: Quiz #14 (10 pts)
"""

import operator
import re

""" ----------------------------------------------------------------------
1. What is the output of the following?
   (5 pts)

[-3, -4, -2, -3, -1, -2]
"""

a = [2, 3, 4]
b = (5, 6)
print reduce(operator.add, map(lambda v : map(lambda w : v - w, b), a))

""" ----------------------------------------------------------------------
2. What is the output of the following?
   (4 pts)

[ab\naab], [a]
"""

s = "b ab\naab 123"
m = re.search("(a+)b([^a]*)(a+)b", s)
print "[" + m.group(0) + "],",
print "[" + m.group(1) + "]"
