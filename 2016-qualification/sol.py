#!/usr/bin/env python

# A.py


from __future__ import print_function
import sys, copy

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



def solver(N):
    if N==0:
       return "INSOMNIA"
    ss = set([str(d) for d in [0,1,2,3,4,5,6,7,8,9]])
    cur = copy.copy(N)
    while True:
        for dgt in str(cur):
            # import pdb; pdb.set_trace()
            if dgt in ss:
                ss.remove(dgt)
                if len(ss)==0:
                    return cur
        cur = cur + N

input_data = open(sys.argv[1])
filename, _ = sys.argv[1].split(".")
output_data = open(filename + ".out","w")

num_tests = int(input_data.readline().rstrip())
for i in range(1,num_tests+1):
    N = int(input_data.readline().rstrip())
    output_data.write("Case #%s: %s\n" % (i, solver(N)))
