#!/usr/bin/env python

"""
CS373: Quiz #7 (10 pts)
"""

""" ----------------------------------------------------------------------
1. In the paper, "A Bug and a Crash" about the Ariane 5, what was the
   software bug?
   (2 pts)

the conversion of a 64-bit number to a 16-bit number
"""

""" ----------------------------------------------------------------------
2. In the paper, "Mariner 1", what was the software bug?
   (2 pts)

the ommission of a hyphen
"""

""" ----------------------------------------------------------------------
3. What is the output of the following?
   (5 pts)

[8, 10]
"""

a = [2, 3, 4]
b = [5, 6, 7]
print [x + y for x in a if x % 2 for y in b if y % 2]
