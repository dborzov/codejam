import pdb
from collections import defaultdict


N=3

A = [
    [2, 3, 5],
    [1, 2, 3],
    [3, 5, 6],
    [2, 3, 4],
    [1, 2, 3],
]

# classify strings
result = []
crosses = []
crosses_inds = []
classified = [False for each in A]
for cur in range(N):
    lowest_value = 9999999999
    lowest_indices = []
    for string_ind, state in enumerate(classified):
        if state:
            continue
        if lowest_value == A[string_ind][cur]:
            lowest_indices.append(string_ind)
        if lowest_value > A[string_ind][cur]:
            lowest_value = A[string_ind][cur]
            lowest_indices = [string_ind]
    for each_cross in lowest_indices:
        classified[each_cross] = True
    crosses.append([A[i] for i in lowest_indices])
    crosses_inds.append([i for i in lowest_indices])


for cur, cross in enumerate(crosses):
    if len(cross) == 1:
        # print cross[0][cur]
        result.append(cross[0][cur])
        continue
    cross_counts = defaultdict(int)
    for line in cross:
        for val in line[cur+1:]:
            cross_counts[val] += 1

    total_counts = defaultdict(int)
    for ind, each_line in enumerate(A):
        if ind in crosses_inds[cur]:
            continue
        total_counts[each_line[cur]] += 1
    # print ' | For ', cur
    # print ' | lines: ', cross
    # print ' | cross_counts: ', cross_counts
    # print ' | total_counts: ', total_counts
    for val, counts in cross_counts.iteritems():
        if counts == 1:
            if total_counts[val] == 0:
                # print val, "(occurs once)"
                result.append(val)
                break
        if counts == 2:
            if total_counts[val] == 1:
                # print val, "(occurs twice)"
                result.append(val)

                break
        if counts > 2:
            print 'shits broken :('
            exit(1)

print result
