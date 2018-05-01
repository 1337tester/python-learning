q = 2**128+51

length = int(q**0.5//1)

for a in range(2, length):
    prime = q
    # if q % a == 0:
    #     print(a, " is a prime")
    #     prime = a
    if a % (q//100) == 0:
        print('.')
print(prime, " is the biggest prime in ", q)

