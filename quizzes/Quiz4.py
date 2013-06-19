#!/usr/bin/env python

"""
CS373: Quiz #4 (10 pts)
"""

""" ----------------------------------------------------------------------
1. Which of the following practices demonstrates effective pair
   programming?
   [All I Really Needed to Know about Pair Programming I Learned in
    Kindergarten]
   (3 pts)

a. Each partner writing separate parts.
b. Each partner writing both parts and then submitting the best.
c. Each partner writing both parts and then submitting the best
   combination.
d. Sharing a monitor and keyboard while coding.
e. One partner writing the interface and tests, the other the
   implementation.

d.
"""

""" ----------------------------------------------------------------------
2. What is the output of the following program?
   (6 pts)

True
False
"""

a = [2, 3, 4]
b = a
b += (5,)
print a == b

a = (2, 3, 4)
b = a
b += (5,)
print a == b
