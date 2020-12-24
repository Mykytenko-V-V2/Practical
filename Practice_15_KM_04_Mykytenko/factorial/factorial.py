def fact(n: int) -> int:
    """
    This function return the factorial of n
    """
    if n < 0:
        raise ArithmeticError("Not exist factorial of n < 0")
    result = 1 
    for i in range(1, n + 1): result *= i
    return result
