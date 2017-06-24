def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    k = len(L)
#    return lambda x: L[a]*x**(k-a-1) for a in range(k)
    return lambda x: sum([L[a]*x**(k-a-1) for a in range(k)])
    
print(general_poly([1, 2, 3, 4])(10))
    
