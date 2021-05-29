import itertools
import pprint

SET1 = ('W10', 'Ubuntu', 'Debian')
SET2 = ('HP', 'Epson', 'Lexmark')
SET3 = ('16GB', '24GB', '64GB')
SET4 = ('6core', '8core', '12core')
SET5 = ('Slow', 'Medium', 'RTX3090')
SET6 = ('HDD', 'SDD', 'HDD+SDD')
SUPERSET = (SET1, SET2, SET3, SET4, SET5, SET6)
SUPERSET_MEMB = set(itertools.chain(*SUPERSET))

# print('superset: ', *superset, sep='\n')
MYLIST = SUPERSET[0:6]
SUPERSET_PRODUCT = set(itertools.product(*MYLIST))
print(SUPERSET_PRODUCT)
# print(*SUPERSET_PRODUCT, sep='\n')
# print(set(itertools.combinations(superset[0], superset[1], 2)))
# print('size of SUPERSET_PRODUCT is ', len(SUPERSET_PRODUCT))

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

# print('all combo ', all_combo(MYLIST))

A = create_pairs(MYLIST)
# A = create_pairs(3)
B = all_combo(SUPERSET)
# print(type(MYLIST))
print(MYLIST)
test_list = (('a', 'b', 'c'), ('d', 'e'), ('g', 'h'))
C = cover_all_pairs(SUPERSET)
# C = cover_all_pairs()

pp = pprint.PrettyPrinter(indent=4)
# print('A', len(A), A)
# print('B', len(B), B)
# print('C', len(C), C)
pp.pprint('A')
pp.pprint(len(A))
pp.pprint(A)

# pp.pprint('B')
# pp.pprint(len(B))
# pp.pprint(B)

pp.pprint('C')
pp.pprint(len(C))
pp.pprint(C)

# for item in A:
#     print(item)

# print(ALL_MEMBERS)
