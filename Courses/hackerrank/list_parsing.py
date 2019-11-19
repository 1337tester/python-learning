"""first input number of following lines
    each following line has a command and parameters for the list
    if the line has only print, the list should be printed
"""


N = int(input())
listka = []
for a in range(1, N+1):
    order = input().split()
    command = order[0]
    args = order[1:]
    if command == "print":
        print(listka)
    else:
        cmd = command + '(' + ",".join(args) + ')'
        eval("listka." + cmd)
