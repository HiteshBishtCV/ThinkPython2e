import time

def has_duplicates_d(lis):
    d= {}
    for i in lis:
        if i in d:
            return True
        else: 
            d[i]=i
    return False

lis= ["a","b","c","d","e","f","g"]
str_time = time.time()
print(has_duplicates_d(lis))
print(f"\n Time required {time.time()-str_time}")
print(has_duplicates_d(lis))
lis= ["a","b","c","d","e",'f']
print(has_duplicates_d(lis))


def has_duplicates2(t):
    """Checks whether any element appears more than once in a sequence.

    Faster version using a set.

    t: sequence
    """
    return len(set(t)) < len(t)
lis= ["a","b","c","d","e","f","g"]
str_time = time.time()
print(has_duplicates2(lis))
print(f"\n Time required {time.time()-str_time}")
