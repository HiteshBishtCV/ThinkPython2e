import math
# function polyline
def polyline(t,n,length,angle):
    """Draws n consequtive line segments differing in angle (degree) of length (px) through turtle(t)"""
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# function arc with better approximation
def arc_b(t,r,angle):
    """Draws arc with radius (r) and angle through turtle (t)"""
   
    # calulation of optimum step size
    arc_length = 2*math.pi*r*angle/360
    n = int(arc_length/4)+1
    step_length = arc_length/n
    step_angle = float(angle)/n
    # making a slight left turn before starting reduces the error
    # caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t,n,step_length, step_angle)
    t.rt(step_angle/2)
    

def petal(t,r,angle):
    """Draws a petal using two arcs using turtle(t) of radius r with angle subtending angle"""
    for i in range(2):
        arc_b(t,r,angle)
        t.lt(180-angle)

def flower(t,n,r,angle):
    """Draws a flower with n petals.
    
    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle(degree) that subtends the arxs
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360/n) # importance of this line for creating line 65 overlaping wiht increasing angle

def main():
    import turtle
    import math

    bob = turtle.Turtle()
    # visulaize using angle 90 and n=4
    # petal(bob,100,90)

    # flower(bob,4,100,90)
    
    
    ###
    # flower(bob,10,100,36)
    # for no overlapping to occur the angle and no of petal should follow angle=360/no of petals
    ###
    # Flower 1 
    bob.pu()
    bob.bk(300)
    bob.pd() 
    flower(bob,7,100,360/7)
    # Flower 2
    bob.pu()
    bob.fd(300)
    bob.pd() 
    flower(bob,10,100,360/(10/2))
    
    #flower 3
    bob.pu()
    bob.fd(300)
    bob.pd() 
    flower(bob,20,200,360/20)

    turtle.mainloop()
if __name__=="__main__":
    main()
else:
    pass

