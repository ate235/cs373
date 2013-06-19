#!/usr/bin/env python

# ------
# Sum.py
# ------

import operator
import sys
import time

print "Sum.py"
print

print sys.version
print

def sum_1 (a) :
    i = 0
    s = 0
    while i != len(a) :
        s += a[i]
        i += 1
    return s

def sum_2 (a) :
    s = 0
    for i in range(len(a)) :
        s += a[i]
    return s

def sum_3 (a) :
    s = 0
    for i in xrange(len(a)) :
        s += a[i]
    return s

def sum_4 (a) :
    p = iter(a)
    s = 0
    try :
        while True :
            s += p.next()
    except StopIteration :
        pass
    return s

def sum_5 (a) :
    s = 0
    for w in a :
        s += w
    return s

def sum_6 (a) :
    return reduce(operator.add, a, 0)

def test_1 (f, c) :
    assert f(c())          == 0
    assert f(c([2]))       == 2
    assert f(c([2, 3]))    == 5
    assert f(c([2, 3, 4])) == 9

def test_2 (f, s) :
    print f.__name__ + " (" + s + ")"
    a = 500 * [1]
    b = time.clock()
    assert f(a) == 500
    e = time.clock()
    print "%5.3f" % ((e - b) * 1000), "milliseconds"
    print

test_1(sum_1, list)
test_1(sum_1, tuple)
#test_1(sum_1, set) # TypeError: 'set' object does not support indexing

test_1(sum_2, list)
test_1(sum_2, tuple)
#test_1(sum_2, set) # TypeError: 'set' object does not support indexing

test_1(sum_3, list)
test_1(sum_3, tuple)
#test_1(sum_3, set) # TypeError: 'set' object does not support indexing

test_1(sum_4, list)
test_1(sum_4, tuple)
test_1(sum_4, set)

test_1(sum_5, list)
test_1(sum_5, tuple)
test_1(sum_5, set)

test_1(sum_6, list)
test_1(sum_6, tuple)
test_1(sum_5, set)

test_1(sum,   list )
test_1(sum,   tuple)
test_1(sum,   set)

test_2(sum_1, "while")
test_2(sum_2, "for in range")
test_2(sum_3, "for in xrange")
test_2(sum_4, "while iter")
test_2(sum_5, "for in")
test_2(sum_6, "reduce operator")
test_2(sum,   "python")

print "Done."

"""
Sum.py

2.7.2 (default, Oct 11 2012, 20:14:37)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)]

2.7.2 (default, Oct 11 2012, 20:14:37)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)]

sum_1 (while)
0.157 milliseconds

sum_2 (for in range)
0.081 milliseconds

sum_3 (for in xrange)
0.066 milliseconds

sum_4 (while iter)
0.164 milliseconds

sum_5 (for in)
0.046 milliseconds

sum_6 (reduce operator)
0.059 milliseconds

sum (python)
0.009 milliseconds

Done.
"""
