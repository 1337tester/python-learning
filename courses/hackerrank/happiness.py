# n_m = input().split()
# n_array = input().split()
# set_a = input().split()
# set_b = input().split()

n_m = 'a'
n_array = ['1', '2', '2', '2', '3']
set_a = ['1', '2', '5', '6', '3']
set_b = ['1', '3']

happiness = 0
for member in set_a:
    if member in n_array: happiness += 1
for member in set_b:
    if member in n_array: happiness -= 1
print(happiness)


happiness = sum([1 for i in n_array if (i in set_a) and (i not in set_b)])

print(happiness)

