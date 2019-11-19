cube = lambda x: x*x*x# complete the lambda function

def fibonacci(n):
    # return a list of fibonacci numbers
    lista = []
    for i in range(n):
        if i == 0: lista.append(0)
        elif i == 1: lista.append(1)
        else: lista.append(lista[-1] + lista[-2])
    return lista

if __name__ == '__main__':
    n = int(5)
    print(list(map(cube, fibonacci(n))))


def test_five(): assert fibonacci(5) == [0, 1, 1, 2, 3]
def test_six(): assert fibonacci(6) == [0, 1, 1, 2, 3, 5]
def test_seven(): assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
