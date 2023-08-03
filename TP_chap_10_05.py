# attempt 1
def bad_is_sorted(t):
    print(t.sort())
    return t==t.sort()
# t.sort() return a none type

print(bad_is_sorted([1,2,2]))
print(bad_is_sorted(['b','a']))

# attempt 2
def bad_1_is_sorted(t):
    j=t
    j.sort()
    print(j)
    return t==j
# list mutable made a copy but ref to same so changing 1 changes another

print(bad_1_is_sorted([1,2,2]))
print(bad_1_is_sorted(['b','a']))


# attempt 3
def is_sorted(t):
    
    j=t.copy() # shallow copy different memory location (but not for nested elements)
    j.sort()
    return t==j
# list mutable made a copy but ref to same so changing 1 changes another

print(is_sorted([1,2,2]))
print(is_sorted(['b','a']))

# another solution using recursion (better solution)
def is_sorted(l):
	if len(l) == 1:
		return True
	else:
		if(l[0] > l[1]):
			return False
		return is_sorted(l[1:])
		
print(is_sorted([1,2,2]))
print(is_sorted(['b','a']))