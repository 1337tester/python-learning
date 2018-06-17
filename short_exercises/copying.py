import copy

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs) # Make a shallow copy
print('xs = ', xs)
print('ys = ', ys)
print(40*'*')

xs.append(['new sublist'])

print('xs = ', xs)
print('ys = ', ys)
print(40*'*')

xs[1][0] = 'X'

print('xs = ', xs)
print('ys = ', ys)
print(40*'*')

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)
xs.append(['new sublist'])
xs[1][0] = 'X'

print('No relation after deep copy')
print('xs = ', xs)
print('zs = ', zs)
print(40*'*')
