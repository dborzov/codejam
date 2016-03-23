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



def solver(p,q):
    match = zip(p, q)
    perfect = zip(sorted(p), sorted(q, key=lambda x: -x))
    log("solver is called with: ", locals())
    return 7

num_tests = input()
for i in range(1,num_tests+1):
    D = int(input())
    p = [int(sym) for sym in raw_input().split(" ")]
    q = [int(sym) for sym in raw_input().split(" ")]

    print("Case #%s: %s" % (i, solver(p,q)))
