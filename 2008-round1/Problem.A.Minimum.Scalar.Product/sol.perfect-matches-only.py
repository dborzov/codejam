#!/usr/bin/env python

# A.py


from __future__ import print_function
import sys
import pdb

DEBUG = False

def log(*args, **kwargs):
    """
        for printing all the execution progress messages into stderr
        (and the output results go to stdout)
    """
    if not DEBUG:
        return
    kwargs["file"] = sys.stderr
    print(*args, **kwargs)

def make_lower_index(a):
    index = {}
    for i, val in enumerate(a):
        u, d = val
        if d not in index:
            index[d] = []
        index[d].append(i)
    return index

def optimal_swipe(match, perfect_index):
    lower_index = make_lower_index(match)
    swipes = set()
    for i, val in enumerate(match):
        up, low = val
        for wanted_low in perfect_index[up]:
            for j in lower_index[wanted_low]:
                if i > j:
                    i,j = j,i
                swipes.add((i,j))
    best_improvement = 0
    best_case = None
    for i,j in swipes:
        improvement = (match[i][0] - match[j][0])*(match[i][1] - match[j][1])
        if improvement > best_improvement:
            best_improvement = improvement
            best_case = (i,j)
    log("match: %s" % match)
    log("optimal swipe: %s [gain %s]" % (best_case, best_improvement))  # really?!
    if best_case is not None:
        i, j = best_case
        new_i = (match[i][0], match[j][1])
        new_j = (match[j][0], match[i][1])
        match[i] = new_i
        match[j] = new_j
    return best_improvement


def solver(upper,lower):
    match = zip(upper, lower)
    scalar_product = sum([u*d for u,d in match])
    perfect = zip(sorted(upper), sorted(lower, key=lambda x: -x))
    perfect_index = {}
    for up, down in perfect:
        if up not in perfect_index:
            perfect_index[up] = []
        perfect_index[up].append(down)
    gain = optimal_swipe(match, perfect_index)
    gain += optimal_swipe(match, perfect_index)
    return scalar_product - gain


num_tests = input()
for i in range(1,num_tests+1):
    D = int(input())
    p = [int(sym) for sym in raw_input().split(" ")]
    q = [int(sym) for sym in raw_input().split(" ")]

    print("Case #%s: %s" % (i, solver(p,q)))
