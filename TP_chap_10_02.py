def cumsum(t):
    "New list with elemsts as cumsum till index i of former list "
    r=[]
    cums=0
    for i in t:
        cums+=i
        r.append(cums)
    return r

t= [1,2,3]
print(cumsum(t))