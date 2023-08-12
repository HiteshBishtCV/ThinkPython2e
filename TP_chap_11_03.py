"""Authors code"""
cache = {}

def ackermann(m, n):
    """Computes the Ackermann function A(m, n)

    See http://en.wikipedia.org/wiki/Ackermann_function

    n, m: non-negative integers
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    try:
        return cache[m, n]
    except KeyError:
        cache[m, n] = ackermann(m-1, ackermann(m, n-1))
        return cache[m, n]

print(ackermann(3, 3))
print(cache)
print(ackermann(4, 0))
print(cache)
print(ackermann(4, 4))
# my comments- he uses cache to store all values encounter before and thus speed up computation for next time