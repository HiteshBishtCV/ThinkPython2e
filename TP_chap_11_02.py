"""Imporove opriginal function to invert using setdefault method"""

#Original
""" def invert_dict(d):
 inverse = dict()
 for key in d:
    val = d[key]
    if val not in inverse:
        inverse[val] = [key]
    else:
        inverse[val].append(key)
    return inverse """

# authors new
def invert_dict(d):
    """"""
    inverse = dict()
    for key, val in d.items():
        inverse.setdefault(val,[]).append(key)       # multiple method stacking 
    return inverse                                    # Solving the none problem by returning empty []

# my
def invert_dict(d):
    """"""
    inverse = dict()
    for key in d:
        inverse[d[key]]=inverse.setdefault(d[key],[])+list(key)      # multiple method stacking 
    return inverse                      

# note the authors uses key and val both which makes things more readable

d={'a':2,'b':1,'c':1,'d':2}
print(invert_dict(d))