import sys

filename, extension = sys.argv[1].split('.')
assert(extension=='in')
src = open(sys.argv[1])
result = open(filename + '.out', 'wb')

def number_of_flips(line, size):
    cur = 0
    flips = 0
    while (cur <= len(line)-size):
        if line[cur]=='-':
            flips += 1
            for i in range(cur, cur+size):
                line[i] = '+' if line[i]=='-' else '-'
        cur += 1
    if any(each=='-' for each in line[cur:]):
        return 'IMPOSSIBLE'
    return str(flips)

num_tests = int(src.readline().rstrip())

for test_idx in range(1,num_tests+1):
    s_line, s_size = src.readline().rstrip().split(' ')
    result.write('Case #%s: %s\n' % (test_idx, number_of_flips(list(s_line), int(s_size))))
