from allpairspy import AllPairs
import itertools
parameters = [
    ['W10', 'Ubuntu', 'Debian'],
    ['HP', 'Epson', 'Lexmark'],
    ['16GB', '24GB', '64GB'],
    ['6core', '8core', '12core'],
    ['Slow', 'Medium', 'RTX3090'],
    ['HDD', 'SDD', 'HDD+SDD']    
]

for i, pairs in enumerate(AllPairs(parameters)): print("{:2d}: {}".format(i, pairs))
print("All combinations: ", len(list(itertools.product(*parameters))))