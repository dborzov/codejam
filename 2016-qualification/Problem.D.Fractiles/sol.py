#!/usr/bin/env python

# A.py


from __future__ import print_function
import sys
import random
import time

DEBUG = True


def get_which_tile(C, K, which_g_variant, position):
    i = position
    for r in range(1,C+1):
        cluster = K**(C-r)
        orig_pos = i /cluster
        if orig_pos==which_g_variant:
            return 'g'
        i = i - cluster* orig_pos
    return 'l'

# import pdb; pdb.set_trace()

input_data = open(sys.argv[1])
filename, _ = sys.argv[1].split(".")
output = open(filename + ".out","w")

num_tests = int(input_data.readline().rstrip())


for tt in range(1,num_tests+1):
    def report_impossible():
      result = "IMPOSSIBLE"
      output.write("Case #%s: %s\n" %(tt, result))

    K, C, S = [int(x) for x in input_data.readline().rstrip().split()]
    total_tiles = K**C
    total_l = (K-1)**C
    limit_S = float(total_tiles) / float(total_tiles - total_l)
    print("---------------------------------------------------------------------------")
    print("test: %s || K= %s, C=%s, limit_S= %s while S=%s" % (tt,K,C,limit_S, S))
    print("-------------> tiles: %s, of those l: %s (ratio: %s )" % (total_tiles, total_l, round(100*total_l/total_tiles)))
    if S < limit_S:
      result = "IMPOSSIBLE"
      output.write("Case #%s: %s\n" %(tt, result))
      continue

    def ok_candidates(candidates):
        def accounted_for(variant):
            for position in candidates:
                tile = get_which_tile(C, K, variant, position)
                if tile == 'g':
                    return True
            return False

        variants = set([g_pos for g_pos in range(K)])
        for variant in variants:
            if not accounted_for(variant):
                return False
        return True

    start = time.time()
    while (True):
        if random.random() > 0.95:
            cluster_size = K**(C-1)
            candidates = [i*cluster_size for i in range(K)]
            if len(candidates) > S:
                candidates= candidates[:S]
        else:
            candidates = set([])
            while True:
                candidates.add(random.randint(0,total_tiles-1))
                if len(candidates) >= S:
                    break


        if ok_candidates(candidates):
            break
        cur_time = time.time()
        if cur_time - start > 40:
            candidates = "Oh"
            break
    if candidates== "Oh":
        result = "IMPOSSIBLE"
    else:
        result = " ".join([str(pos + 1) for pos in candidates])
    print("result is: ", result)
    output.write("Case #%s: %s\n" %(tt, result))
