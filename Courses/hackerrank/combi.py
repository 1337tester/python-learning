from itertools import combinations
WORD, SIZE = input().split()
# WORD, SIZE = 'HACK 2'.split()
for a in range(1, int(SIZE)+1):
    for i in combinations(sorted(WORD), int(a)):
        print(''.join(i))
