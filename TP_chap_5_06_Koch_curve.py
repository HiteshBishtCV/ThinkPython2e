"""
Excercise 5-6
"""
import turtle

def koch_curve(t,x):
    if x<3:
        t.fd(x)
    else:
        for i in [-60,120,-60,0]:

            koch_curve(t,x/3)
            t.lt(i)
        

def snowflake(t,x):
    """ Draws snoflake outline with tutle t of side length x"""
    for i in range(3):
        koch_curve(t,x)
        t.lt(120)



def main():
    bob = turtle.Turtle()
    
    turtle.tracer(10,0)
    # Syntax : turtle.tracer(n=None, delay=None)
    # n: If n is given, only each n-th regular screen update is really performed.
    # delay: sets delay value
    koch_curve(bob,300)
    
    turtle.mainloop()

if __name__=="__main__":
    main()
else:
    pass