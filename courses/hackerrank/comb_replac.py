from itertools import combinations_with_replacement
# word, length = input().split()

word = 'hack'
length = 2
combo = list(combinations_with_replacement(sorted(word),int(length)))
for a in combo:
    print(*a, sep='')
