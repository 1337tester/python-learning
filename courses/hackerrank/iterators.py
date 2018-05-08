import itertools
length = 4
letters = 'a a c d'.split()
selected = 2
# length = int(input())
# letters = input().split()
# selected = int(input())
# print(length, letters, selected)
present, absent = 0, 0
for combo in itertools.combinations(letters, selected):
    if 'a' in combo: present += 1
    else: absent += 1
total = present + absent
print(present/total)
