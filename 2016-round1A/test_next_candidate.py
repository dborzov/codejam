column_candidates = [['a1','a2'], ['b1', 'b2'], ['c1','c2'], ['d'],None, ['f1', 'f2']]
cur_candidate_indices = [0 for cc in column_candidates]
# traverse through all the candidates
def next_candidate():
    carry_over = 0
    while True:
        if column_candidates[carry_over] is not None and cur_candidate_indices[carry_over] < len(column_candidates[carry_over])-1:
            cur_candidate_indices[carry_over] += 1
            return True
        cur_candidate_indices[carry_over] = 0
        if carry_over == len(column_candidates) -1:
            return False
        carry_over += 1

while True:
    candidate = [column_candidates[column_i][ind] if column_candidates[column_i] else None for column_i, ind in enumerate(cur_candidate_indices)]
    print candidate
    if not next_candidate():
        break
