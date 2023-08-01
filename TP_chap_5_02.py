"""
Think python Excercise 5-2
"""

def check_fermat(a,b,c,n):
    """
    Check whether Fermat's last theorem holds
    Precondition a,b,c are positive integers
    n greater than 2
    """
    if n>2 and a>0 and b>0 and c>0:
        lhs = a**n + b**n
        rhs = c**n
        if lhs==rhs:
            print("fermat last thereom is false")
        else:
            print("Fermat last theorem holds")
    else:
        print("precondition doesn't meet")

def user_in_check_fermat():
    """
    Takes values to check in fermat's last theorem
    """
    a = int(input("Enter value of a in a^n+b^n=c^n expression:\n"))
    b = int(input("Enter value of b in a^n+b^n=c^n expression:\n"))
    c = int(input("Enter value of c in a^n+b^n=c^n expression:\n"))
    n = int(input("Enter value of d in a^n+b^n=c^n expression:\n"))

    if isinstance(a,int) and isinstance(b,int) and isinstance(c,int) and isinstance(n,int):
        check_fermat(a,b,c,n)
    else:
        print("Input vlues doesn't meet the precondition")

def main():
    user_in_check_fermat()

    
if __name__=="__main__":
    main()
else:
    pass
        
