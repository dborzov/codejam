#!/usr/bin/env python

Table = {
    "1": {"1":"1", "i":"i", "j": "j", "k": "k"},
    "i": {"1":"i","i":"-1", "j": "k", "k": "-j"},
    "j": {"1":"j","i":"-k", "j": "-1", "k": "i"},
    "k": {"1":"k","i":"j", "j": "-i", "k": "-1"}
}


def multiply_rules(a,b):
    return Table[a][b]


def strip_negative(a):
    if len(a) == 1:
        return 1, a
    else:
        return -1, a[1]


def negate(a):
    if len(a) == 1:
        return "-" + a
    else:
        return a[1]

def multiply(a,b):
    signA, symA = strip_negative(a)
    signB, symB = strip_negative(b)
    result = multiply_rules(symA, symB)
    return result if signA*signB != -1 else negate(result)

def pow(a, p):
    times = p % 4
    if times==0:
        return a
    cur = a
    for _ in range(times-1):
        cur = multiply(cur,a)
    return cur


def solver(X, expr):
    # print "~~~~~~~"
    # print "called with %s, and \"%s\"" % (X, expr)
    if len(expr)*X <3:
        return "NO"
    set_of_i_breaks = []
    set_of_k_breaks = []
    PrefixSum = []
    cur = "1"
    for s in expr: 
        cur = multiply(cur, s)
        if cur == "i":
            set_of_i_breaks.append({"X":0,"pos": len(PrefixSum)})
        if cur == "k":
            set_of_k_breaks.append({"X":0,"pos": len(PrefixSum)})
        PrefixSum.append(cur)
    M = PrefixSum[-1]
    # print "Prefix sum: %s " % PrefixSum
    if pow(M,X) != "-1":
        return "NO"
    Ms = [M, pow(M,2), pow(M,3)]

    # second repetition i breaks
    if X>1:
        possible_whole_prefixes = min(X-1,3)
        for ind, prefix_sum in enumerate(PrefixSum):
            for pp in range(1,possible_whole_prefixes+1):
                prod = multiply(Ms[pp-1], prefix_sum)
                if prod == "i":
                    set_of_i_breaks.append({"X":pp,"pos": ind})
                if prod == "k":
                    set_of_k_breaks.append({"X":pp,"pos": ind})



    # print "set of i breaks: %s " % set_of_i_breaks
    # print "set of k breaks: %s " % set_of_k_breaks

    if len(set_of_i_breaks) == 0 or len(set_of_k_breaks) == 0:
        return "NO"
    LEFTIEST_i = min([breaker["X"]*len(expr) + breaker["pos"] for breaker in set_of_i_breaks])

    # calculate rightiest
    k_breakers = []
    for breaker in set_of_k_breaks:
        padding_of_1s = (X - (breaker["X"]+1)) / 4 if X - (breaker["X"]+1)>0 else 0


        k_breakers.append((4*padding_of_1s + breaker["X"])*len(expr) + breaker["pos"])
    RIGHTIEST_k = max(k_breakers)
    # print "print of L&R: %s, %s " % (LEFTIEST_i, RIGHTIEST_k)
    if LEFTIEST_i < RIGHTIEST_k:
        return "YES"
    else:
        return "NO"

num_tests = input()
for i in range(1,num_tests+1):
    L, X = str(raw_input()).rstrip().split(" ")
    expr = raw_input().rstrip()
    print "Case #%s: %s" % (i, solver(int(X), expr))
 
