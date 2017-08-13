import re
# S = input()
# k = input()

S = 'abababbaba'
k = 'aa'

result = (-1, -1)
index = 0

while re.search(k, S):
    m = re.search(k, S, )
    result = (m.start() + index, m.start() + len(k) - 1 + index)
    print(result)
    S = S[m.start()+1:]
    index += m.start() + 1
    # print('debug: ', S, index)

if index == 0: print((-1,-1))


"""
S = raw_input()
k = raw_input()
import re
pattern = re.compile(k)
r = pattern.search(S)
if not r: print "(-1, -1)"
while r:
    print "({0}, {1})".format(r.start(), r.end() - 1)
    r = pattern.search(S,r.start() + 1)
"""
