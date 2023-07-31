
# square function for tutle
def square(t, length):
    """"Takes in a turtle(t) and draws square of length"""
    for i in range(4):
        t.fd(length)
        t.lt(90)

import turtle
import math

# function polyline
def polyline(t,n,length,angle):
    """Draws n consequtive line segments differing in angle (degree) of length (px) through turtle(t)"""
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# function polygon
def polygon(t,n,length):
    """Draws a regular n sided polygon of length through turtle (t)"""
    angle=360/n
    polyline(t,n,length,angle)

# function arc
def arc(t,r,angle):
    """Draws arc with radius (r) and angle through turtle (t)"""

    # calulation of optimum step size
    arc_length = 2*math.pi*r*angle/360
    n = int(arc_length/4)+1
    step_length = arc_length/n
    step_angle = float(angle)/n
    polyline(t,n,step_length, step_angle)

# function arc with better approximation
def arc_b(t,r,angle):
    """Draws arc with radius (r) and angle through turtle (t)"""
    t.color(1,0,0)
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
    t.color(0,0,0)  
    # have made change inside bob (turtle object) inside the function which sticks even outside
    # color remains red for third arc also 

""" bob = turtle.Turtle()
arc(bob,100,360)
arc_b(bob,100,360)
arc(bob,100,360) """

# circle function

def circle(t, r):
    cirmcumference = 2*math.pi*r
    n = int(cirmcumference/4)+1
    step_length = cirmcumference/n
    step_angle = 360/n
    # making a slight left turn before starting reduces the error
    # caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t,n,step_length, step_angle)
    t.rt(step_angle/2)

""" bob = turtle.Turtle()
circle(bob,100) """

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__=="__main__":
    bob = turtle.Turtle()
    # draw a circle centered on the origin
    radius = 100
    bob.pu()
    bob.fd(radius)
    bob.pd()
    circle(bob, radius)
    turtle.mainloop()