import turtle
bob = turtle.Turtle()
bob.speed(0)
bob.color('red')

def draw(bob, length, n):
    if n == 0:
        return
    angle = 50
    bob.fd(length * n)
    bob.lt(angle)
    draw(bob, length, n - 1)
    bob.rt(angle*2)
    draw(bob, length, n - 1)
    bob.lt(angle)
    
    bob.bk(length * n)



draw(bob, 9, 7)

turtle.mainloop()