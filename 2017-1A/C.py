import sys, bisect

filename, extension = sys.argv[1].split('.')
assert(extension=='in')
src = open(sys.argv[1])
result = open(filename + '.out', 'wb')

num_tests = int(src.readline().rstrip())
for test_idx in range(1,num_tests+1):
    HD, AD, HK, AK, B, D = [int(each) for each in src.readline().split(' ')]
    print locals()
