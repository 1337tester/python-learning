from itertools import permutations
WORD, LENGTH = input().split()
for i in sorted(permutations(WORD, int(LENGTH))):
    print(''.join(i))
