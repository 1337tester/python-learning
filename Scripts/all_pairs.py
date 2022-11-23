import itertools

operation_system = ('W10', 'Ubuntu', 'Debian')
manufacturer = ('HP', 'Epson', 'Lexmark')
ram = ('16GB', '24GB', '64GB')
cpu = ('6core', '8core', '12core')
graphics = ('Slow', 'Medium', 'RTX3090')
storage = ('HDD', 'SDD', 'HDD+SDD')
SUPERSET = (operation_system, manufacturer, ram, cpu, graphics, storage)

def create_pairs(set_of_sets):
    """Returns pairs from set_of_sets and all_members of that set"""
    # combine subsets into a set
    try:
        all_members = set(itertools.chain(*set_of_sets))
    except Exception as e_xception:
        raise e_xception
    #create all possible pairs
    all_pairs = set(itertools.combinations(all_members, 2))
    unique_pairs = list(all_pairs)
    #deletes pair from the list which members both belong to the same list
    for group in set_of_sets:
        for pair in all_pairs:
            if set(pair).issubset(group):
                unique_pairs.remove(pair)
    return unique_pairs

def all_combo(set_of_sets):
    """Returns a cartesian product of a set of sets"""
    return list(itertools.product(*set_of_sets))

def cover_all_pairs(set_of_sets):
    """
    Takes set of complete combinations of a product and set of all_pairs
    returns an optimal subset of former set containing all the pairs
    """
    set_of_pairs = create_pairs(set_of_sets)
    # print("Number of pairs: ", len(set_of_pairs))
    all_comb = all_combo(set_of_sets)
    # print("Number of combinations: ", len(all_comb))
    efficient_comb = []
    for pair in set_of_pairs:
        for group in all_comb:
            if set(pair).issubset(group) and group not in efficient_comb:
                efficient_comb.append(group)
                break
    return efficient_comb



efficient_pairs = cover_all_pairs(SUPERSET)
all_comb = all_combo(SUPERSET)

for pair in efficient_pairs: print(pair)
print("Combinations to cover all pairs: ", len(efficient_pairs))
print("All combinations: ", len(all_comb))
print(15*"*")

from allpairspy import AllPairs
parameters = [
    ['W10', 'Ubuntu', 'Debian'],
    ['HP', 'Epson', 'Lexmark'],
    ['16GB', '24GB', '64GB'],
    ['6core', '8core', '12core'],
    ['Slow', 'Medium', 'RTX3090'],
    ['HDD', 'SDD', 'HDD+SDD']    
]

for i, pairs in enumerate(AllPairs(parameters)): print("{:2d}: {}".format(i, pairs))