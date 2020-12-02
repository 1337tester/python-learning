import itertools

SET1 = ('italy', 'ireland', 'norway', 'denmark', 'spain')
SET2 = ('SFMC', 'IOS', 'Android', 'Web')
SET3 = ('google', 'FB', 'apple pay')
SET4 = ('sign up', 'order flow', 'settings')
SET5 = ('on', 'off')
SET6 = ('mail', 'push')
SUPERSET = (SET1, SET2, SET3, SET4, SET5, SET6)
SUPERSET_MEMB = set(itertools.chain(*SUPERSET))

# print('superset: ', *superset, sep='\n')
MYLIST = SUPERSET[0:3]
SUPERSET_PRODUCT = set(itertools.product(*MYLIST))
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
print('A', len(A), A)
print('B', len(B), B)
print('C', len(C), C)

# for item in A:
#     print(item)

# print(ALL_MEMBERS)
