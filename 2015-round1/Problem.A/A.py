#!/usr/bin/env python

# A.py


from __future__ import print_function
import sys

DEBUG = True

def log(*args, **kwargs):
    """
        for printing all the execution progress messages into stderr
        (and the output results go to stdout)
    """
    if not DEBUG:
        return
    kwargs["file"] = sys.stderr
    print(*args, **kwargs)



def solver(P):
    log("called with ", P)
    min_rate = 0
    m1 = 0
    for i in range(len(P)-1):
        eaten = P[i] - P[i+1] if P[i]> P[i+1] else 0
        m1 += eaten
        if eaten > min_rate:
            min_rate = eaten
            log("reasign min_rate to  ", min_rate,"at ", i)

    m2 = 0
    for i in range(len(P)-1):
        m2 += min(P[i], min_rate)

    return "%s %s" % (m1, m2)




num_tests = input()
for i in range(1,num_tests+1):
    D = int(input())
    P= [int(sym) for sym in raw_input().split(" ")]
    print("Case #%s: %s" % (i, solver(P)))
