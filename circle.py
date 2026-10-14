import turtle
import math

def polygon(t, n, length):
    """Draw a polygon with n sides."""
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        

def circle(t, r):
    """Draw a circle with radius r."""
    circumference = 2 * math.pi * r
    n = 50 
    length = circumference / n
    polygon(t, n, length)

t = turtle.Turtle()
t.speed(10)
t.color("blue")

# Draw a circle
circle(t, 70)

turtle.mainloop()
