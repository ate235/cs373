#!/usr/bin/env python

"""
CS373: Quiz #5 (10 pts)
"""

""" ----------------------------------------------------------------------
1. In pair programming which of the partners should do most of the
   driving?
   [XP: Ch. 12, Pg. 90]
   (2 pts)

the one who is least sure of what's being done
"""

""" ----------------------------------------------------------------------
2. What are the two most common problems with releasing changes?
   [XP: Ch. 15, Pg. 124-125]
   (2 pts)

slow merges
lost changes
"""

""" ----------------------------------------------------------------------
3. What is the output of the following program?
   (4 pts)

2 2
3 3
"""

a = [2, 3, 4]
p = iter(a)
q = iter(a)
print p.next(),
print q.next()
print p.next(),
print q.next()
