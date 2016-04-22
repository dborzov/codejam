import pdb, sys
from collections import defaultdict

def solve_thingy(N, A):
    result = []
    counts = {}
    for line in A:
        for val in line:
            counts[val] = counts.get(val,0) + 1
    for key, count in counts.iteritems():
        if count % 2 == 0:
            continue
        result.append(key)
    result = sorted(result)
    return " ".join([str(val) for val in result])

input_data = open(sys.argv[1])
filename, _ = sys.argv[1].split(".")
output_data = open(filename + ".out","w")

num_tests = int(input_data.readline().rstrip())
for i in range(1,num_tests+1):
    N = int(input_data.readline().rstrip())
    A = []
    for _ in range(2*N-1):
        A.append([int(sym) for sym in input_data.readline().rstrip().split(" ")])
    output_data.write("Case #%s: %s\n" % (i, solve_thingy(N, A)))
