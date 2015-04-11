#!/usr/bin/env python

def standing_ovation(S_max, S):
    missing = 0
    extra = 0
    for i in S:
        extra += (i - 1) if i>1 else 0
        if i==0:
            if extra>0:
                extra -= 1
            else:
                missing += 1
    return missing

num_tests = input()
for i in range(1,num_tests+1):
    S_max, lstring = str(raw_input()).rstrip().split(" ")
    S = [int(sym) for sym in lstring]
    print "Case #%s: %s" % (i, standing_ovation(S_max, S)) 
