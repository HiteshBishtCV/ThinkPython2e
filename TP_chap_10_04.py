def chop(t):
    """modifies list but return none"""
    del t[::len(t)-1]

t = [1,2,3,4]
chop(t)
print(t)