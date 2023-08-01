import math

def estimate_pi():
    """
    estimate pi using ramajunam's formula
    """
    estimate = 0
    k=0
    diff=1 # can't keep zero otherwise code won't run
    while diff>1e-15:
        in_pi = math.factorial(4*k)*(1103+26390*k)/((math.factorial(k)*396**(4*k)))
        k+=1
        estimate = 9801/(in_pi*2*math.sqrt(2))
        diff = math.pi - estimate
    return estimate

def main():
    print(estimate_pi())

if __name__=="__main__":
    main()
else:
    pass