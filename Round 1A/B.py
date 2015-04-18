#!/usr/bin/env python

# C.py


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




def solver(N, M):
    N = N-1
    def HowManyDoneInXMinutes(X):
        return sum([X/speed for speed in M])


    def WhichOnes(X):
        return map(lambda speed: X % speed==0, M)

    def LowestAvalBarber(X, which):
        for i, speed in enumerate(M):
            if X % speed == 0:
                if which >0:
                    which -= 1
                else:
                    return i+1
        return "fuck"

    last = 25*(N + 100)
    first = 0
    est = 3654564564564564575684535
    while(not (est == N or first + 1 == last)):
        X = first + (last - first) /2
        est = HowManyDoneInXMinutes(X)
        if est > N:
            last = X
        if est < N:
            first = X


    while(HowManyDoneInXMinutes(X) >= N):
        X -= 1
    X = X+1

    if HowManyDoneInXMinutes(X) > N:
        res = N - HowManyDoneInXMinutes(X-1)
    else:
        res = 0
# 91036146
    if est != N:
        log("solver is called with: ", N, " und ", M)
        log("iteratin within [", first, "..", last, "] and done(", X,")=",est, " while N=",N, "bounds (", HowManyDoneInXMinutes(first),",", HowManyDoneInXMinutes(last),")")
        log('~~~~~~~~~~~~~~~')
        log("X=", X, "done(", HowManyDoneInXMinutes(X), ")")
        log("which ones: ", WhichOnes(X))
        log("while for X=", X-1, "done(", HowManyDoneInXMinutes(X-1), ")")
        log("which ones: ", WhichOnes(X-1))
        log("res is ", res)
        log('~~~~~~~~~~~~~~~')
        return LowestAvalBarber(X-1, res-1)


    return LowestAvalBarber(X, res)





    return "Hi "

num_tests = input()
for i in range(1,num_tests+1):
    N = int(raw_input().split(" ")[1])
    M= [int(sym) for sym in raw_input().split(" ")]
    print("Case #%s: %s" % (i, solver(N, M)))
