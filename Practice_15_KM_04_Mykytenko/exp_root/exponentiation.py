def _exp(n: float, k: int) -> float:
    """
    The function returns the exponentiation of n to k
    """
    if k == 0 and n == 0:
        raise ArithmeticError("Not exist the exponentiation of 0 to 0")
    result: float = 1
    for _ in range(k):
        result *= n
    else:
        return result
         
            
exp2 = lambda n: _exp(n, 2) #The function returns the exponentiation of n to 2
exp3 = lambda n: _exp(n, 3) #The function returns the exponentiation of n to 3
