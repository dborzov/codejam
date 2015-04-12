#!/usr/bin/env python


def specials(P):
    alternatives = []
    for key in P:
        if key == 1:
            continue
        shuffled = P.copy()
        taken = key / 2
        residual = key - taken

        if shuffled[key] >1:
            shuffled[key] -= 1
        else:
            del shuffled[key] 

        if taken in shuffled:
            shuffled[taken] += 1
        else:
            shuffled[taken] = 1

        if residual in shuffled:
            shuffled[residual] += 1
        else:
            shuffled[residual] = 1
        alternatives.append(shuffled)
    return alternatives

def standard_minute(P):
    return {key-1: P[key] for key in P if key>1}


def minimal_minutes(P):
    default = max([key for key in P])
    if default > 2:
        let_them_eat = minimal_minutes(standard_minute(P)) +1
        alternatives = [minimal_minutes(each)+ 1 for each in specials(P)]
        # print "~~~~~~~~~"        
        # print "minimal_minutes called with: %s" % (P)
        # print "  if let them eat we get: %s (%s mins)" % (R, let_them_eat)
        # print "  if shuffle: %s  (%s mins)" % (specials(P), min(alternatives))
        # print "~~~~~~~~~"
        return min([let_them_eat] + alternatives)
    else:
        return default


num_tests = input()
for i in range(1,num_tests+1):
    D = int(input())
    P= {}
    for sym in raw_input().split(" "):
        if int(sym) in P:
            P[int(sym)] += 1
        else:
            P[int(sym)] = 1
    print "Case #%s: %s" % (i, minimal_minutes(P))


