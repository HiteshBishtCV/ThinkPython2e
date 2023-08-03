def middle(t):
    """Remove first and last elements"""
    del t[::len(t)-1]
    return t

t = [1,2,3,4,5]
print(middle(t))