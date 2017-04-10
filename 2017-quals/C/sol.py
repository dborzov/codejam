import sys, heapq

filename, extension = sys.argv[1].split('.')
assert(extension=='in')
src = open(sys.argv[1])
result = open(filename + '.out', 'wb')

def last_stall(N,K):
    # print N, K
    s_min = (N - 1) // 2
    s_max = N - 1 - s_min
    if K==1: return s_max, s_min
    sub_k = (K -1) - (K-1) // 2
    return last_stall(s_max, sub_k) if K % 2 == 0 else last_stall(s_min, sub_k)


def shift(K):
    base = 2**len("{0:b}".format(K)[1:])
    residue = K-base
    return K+2*residue


num_tests = int(src.readline().rstrip())

for test_idx in range(1,num_tests+1):
    N, K = [int(each) for each in src.readline().split(' ')]
    stall_min, stall_max = last_stall(N, K)
    result.write('Case #%s: %s %s\n' % (test_idx, stall_min, stall_max))
