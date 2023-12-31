import turtle

def draw(t,length,n):
    if n==0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t,length,n-1)
    t.rt(2*angle)
    draw(t,length,n-1)
    t.lt(angle)
    t.bk(length*n)

def main():
    bob = turtle.Turtle()
    draw(bob,5,5)

    turtle.mainloop()

if __name__=="__main__":
    main()
else:
    pass