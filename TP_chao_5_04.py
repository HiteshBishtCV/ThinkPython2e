"""
Excercise 5-4
"""
def recurse(n,s):
    if n==0:
        print(s)
    else:
        recurse(n-1,n+s)

recurse(3,1)

"""
0: Output  6 
1: infinite looping
2: Prints the sum of all natural no till the given number no (n) + any other no (s)
"""