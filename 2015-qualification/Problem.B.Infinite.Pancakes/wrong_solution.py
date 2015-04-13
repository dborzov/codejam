#!/usr/bin/env python

def minimal_minutes(P, log=False):
    if len(P)==0:
        return 0
    P = sorted(P, key=lambda x: -x)
    let_them_eat = [i-1 for i in P if i>1]
    optimal_mins = minimal_minutes(let_them_eat)

    if P[0] > 1:
        j =P[0]/2
        new_P = P[:]
        new_P[0] = new_P[0] - j
        new_P.append(j)
        variant_time = minimal_minutes(new_P) 
        if variant_time < optimal_mins:
            optimal_mins = variant_time
            if log:
                print "that is the optimal division: %s" % new_P
    return optimal_mins + 1




num_tests = input()
for i in range(1,num_tests+1):
    D = int(input())
    P= [int(sym) for sym in raw_input().split(" ")]
    print P
    print "Case #%s: %s" % (i, minimal_minutes(P, log=True))

