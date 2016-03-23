#!/usr/bin/env python

# C.py


from __future__ import print_function
import sys

DEBUG = True

def log(*args, **kwargs):
    if not DEBUG:
        return
    kwargs["file"] = sys.stderr
    print(*args, **kwargs)




def solver(N, M):
    def OutOfLine(X):
        return sum((X-1)/speed +1 for speed in M)

    def WhichBarber(X, num):
        for i, barb in enumerate(M):
            if X % barb != 0:
                continue
            if num > 1:
                num -= 1
            else:
                return i+1
        return "fuck"

    def AvailableBarbers(X):
        return [i+1 if X % m ==0 else "x" for i, m in enumerate(M)]

    low = 0
    high = (N + 1) * 100000
    while (abs(high - low) > 1):
        X = low + (high - low)/2
        val = OutOfLine(X)
        if val >= N:
            high = X
        if val < N:
            low = X

    log("~~~~~~~~~~~~~~~~~")
    log("range is: (%s,%s) with bounds for %s in [%s, %s]" % (low, high, N, OutOfLine(low), OutOfLine(high)))
    threshold_val = OutOfLine(low)
    res = N - threshold_val
    log("now low is even: D(%s)=%s, R(low)=%s" % (low, threshold_val, res))
    log("M=",M)
    log("M=",AvailableBarbers(low))
    log("~~~~~~~~~~~~~~~~~")
    return WhichBarber(low, res)


num_tests = input()
for i in range(1,num_tests+1):
    N = int(raw_input().split(" ")[1])
    M= [int(sym) for sym in raw_input().split(" ")]
    print("Case #%s: %s" % (i, solver(N, M)))
