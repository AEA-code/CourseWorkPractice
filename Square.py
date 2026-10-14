#Write a function called square that takes a parameter named t, which is a turtle. It should use the turtle to draw a square.
#Write a function call that passes bob as an argument to square, and then run the program again.
import turtle
def square(t,length):
    for _ in range(7):
        t.lt(length)
        t.bk(50)
        t.lt(25)
        t.fd(50)
        t.rt(180)
        #t.fd(50)
        #t.bk(50)
        

t = turtle.Turtle()
square(t,50)

turtle.speed(10)
turtle.mainloop()


# print("hi"*5)