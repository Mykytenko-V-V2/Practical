def _root(n: float, k:int) -> float:
    if k % 2 == 0:
        if n < 0:
            raise ArithmeticError("not a real root")
    if k != 0:
        return n**(1/k)
    else:
         raise ArithmeticError("there is no 0th root of n")

root2 = lambda n: _root(n, 2)
root3 = lambda n: _root(n, 3)
