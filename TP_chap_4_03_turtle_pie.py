import math
import turtle

def draw_iso_triangle(t,r,alpha,beta,base):
    """Draws a isoscles tringle with base length (base) and side (r) and angle (alpha)
    t: turtle
    r: side of isosceles triangle
    alpha: angle of isocles triangle
    beta: other angles of isoceles triangle
    base: length of base 
    """
    t.fd(r)
    t.lt(180-beta)
    t.fd(base)
    t.lt(180-beta)
    t.fd(r)
    t.lt(180-alpha)

def draw_pie(t,r,n):
    """Draws a pie using isocles triangles
    
    t: turtle
    r: side
    n: no of pies
    """
    alpha = 360/n
    beta = (1/2)*(180-alpha)
    base = 2*r*math.sin(math.pi*alpha/(2*180))
    for i in range(n):
        draw_iso_triangle(t,r,alpha,beta,base)
        t.lt(alpha)

def main():
    bob = turtle.Turtle()
    bob.pu()
    bob.bk(300)
    bob.pd() 
    bob.lt(180)
    draw_pie(bob,100,5)
    bob.lt(180)


    bob.pu()
    bob.fd(300)
    bob.pd() 
    bob.lt(90)
    draw_pie(bob,100,6)
    # the draw pie commands will make the turtle face in the direction it originally started in the end

    bob.rt(90)
    bob.pu()
    bob.fd(300)
    bob.pd() 
    bob.lt(180)
    draw_pie(bob,100,7) 

    turtle.mainloop()

if __name__=="__main__":
    main()
else:
    pass