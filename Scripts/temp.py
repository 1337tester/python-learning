if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tuplac = tuple(integer_list)[0:n]
    print(hash(tuplac))