import time
def has_duplicates(lis):
    """Return true if any duplicates present"""
    for i in lis:
        lis.remove(i)  # this method doesn't return anything just modifies the list
        if i in lis:
            return True
        
lis= ["a","b","c","d"]
str_time = time.time()
print(has_duplicates(lis))
print(f"\n Time required {time.time()-str_time}")

lis= ["a","b","c","d","a"]
print(has_duplicates(lis))



