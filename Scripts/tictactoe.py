import sys

def where_defend(opp_has):
    """random docstring"""
    return opp_has + 1


# game loop
opp = []
me = []
while True:
    unused = []
    opponent_row, opponent_col = [int(i) for i in input().split()]
    opp.append((opponent_row, opponent_col))
    valid_action_count = int(input())
    print("oponnent: ", opp, file=sys.stderr)
    for i in range(valid_action_count):
        row, col = [int(j) for j in input().split()]
        unused.append((row, col))
    print(unused[0][0], unused[0][1])
    me.append((unused[0][0], unused[0][1]))
    print("unused: ", unused, file=sys.stderr)
    print("me: ", me, file=sys.stderr)
    #if 1 in row and 1 in col:
     #   print("1 1")
