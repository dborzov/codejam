import sys, bisect

filename, extension = sys.argv[1].split('.')
assert(extension=='in')
src = open(sys.argv[1])
result = open(filename + '.out', 'wb')

num_tests = int(src.readline().rstrip())
def draw(table):
    for row in table: print ''.join(row)

for test_idx in range(1,num_tests+1):
    R, C = [int(each) for each in src.readline().split(' ')]
    table = []
    children = []
    for row_number in range(R):
        row = [each for each in src.readline().rstrip()]
        for column_number, each in enumerate(row):
            if not(each=='?'):
                children.append((row_number, column_number))
        table.append(row)
    print '[%sx%s]' % (R, C)

    column_brackets = []
    row_brackets = []
    for _ in range(R): row_brackets.append([])
    for _ in range(C): column_brackets.append([])
    # print 'Children:', children
    for x, y in children:
        row_brackets[x].append(y)
        column_brackets[y].append(x)
    for each in row_brackets:
        each.sort()
    for each in column_brackets:
        each.sort()
    def column_limits(x,y):
        left_idx = bisect.bisect_left(row_brackets[x],y)
        left = 0 if left_idx==0 else row_brackets[x][left_idx-1]
        right = row_brackets[x][left_idx+1] if ((left_idx +1) < len(row_brackets[x])) else C
        return left, right

    def row_limits(x,y):
        left_idx = bisect.bisect_left(column_brackets[y],x)
        left = 0 if left_idx==0 else column_brackets[y][left_idx-1]
        right = column_brackets[y][left_idx+1] if ((left_idx +1) < len(column_brackets[y])) else R
        return left, right



    blanks = R*C - len(children)

    def check_only_one(left_x, right_x, left_y, right_y, letter, letter_x, letter_y):
        for ch_x, ch_y in children:
            if (left_x<=ch_x <= right_x) and (left_y <=ch_y <= right_y):
                if (letter_x==ch_x) and (letter_y==ch_y):
                    continue
                return False
        return True
        for dx in range(left_x, right_x+1):
            for dy in range(left_y, right_y+1):
                if not((table[dx][dy]==letter) or (table[dx][dy]=='?')):
                    return False
        return True

    def fill(table, left_x, right_x, left_y, right_y, letter):
        for dx in range(left_x, right_x+1):
            for dy in range(left_y, right_y+1):
                table[dx][dy] = letter

    def clear(table, left_x, right_x, left_y, right_y, letter):
        for dx in range(left_x, right_x+1):
            for dy in range(left_y, right_y+1):
                table[dx][dy] = '?'

    def backgate(table, child, filled_count):
        if child==len(children):
            if filled_count==blanks:
                return True
            return False
        x,y = children[child]
        letter = table[x][y]
        column_low, column_high = column_limits(x,y)
        row_low, row_high = row_limits(x,y)
        print 'FOR LETTER ', letter, ' the y limits are: ', column_low, column_high
        for left_x in range(row_low, x+1, 1):
            for right_x in range(row_high-1, x-1, -1):
                for left_y in range(column_low, y+1, 1):
                    for right_y in range(column_high-1, y-1, -1):
                        empty = check_only_one(left_x, right_x, left_y, right_y, letter, x, y)
                        if not empty:
                            continue
                        fill(table, left_x, right_x, left_y, right_y, letter)
                        # print 'at ', letter, ' we get: '
                        # draw(table)
                        cur_fillings = (right_y +1 - left_y)*(right_x +1 - left_x) - 1
                        if child < len(children):
                            match = backgate(table, child + 1, filled_count + cur_fillings)
                            if match:
                                return match
                        clear(table, left_x, right_x, left_y, right_y, letter)
                        table[x][y] = letter
    draw(table)
    backgate(table, 0, 0)
    result.write('Case #%s:\n' % test_idx)
    print 'Case #%s:\n' % test_idx
    for row in table:
        result.write(''.join(row))
        result.write('\n')
