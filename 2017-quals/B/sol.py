import sys

filename, extension = sys.argv[1].split('.')
assert(extension=='in')
src = open(sys.argv[1])
result = open(filename + '.out', 'wb')

def last_tidy(number):
    while True:
        idx = tidyness(number)
        if (idx is None):
            return int(''.join([str(each) for each in number]))
        number[idx]= number[idx] -1
        for tail in range(idx+1,len(number)):
            number[tail]=9


def tidyness(number):
    cur = 0
    while cur < (len(number)-1):
        if number[cur] > number[cur+1]:
            return cur
        cur += 1
    return None

num_tests = int(src.readline().rstrip())

for test_idx in range(1,num_tests+1):
    number = [int(each) for each in src.readline().rstrip()]
    result.write('Case #%s: %s\n' % (test_idx, last_tidy(number)))
