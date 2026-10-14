"""Draw a regular polygon using the turtle graphics module.

This module defines a helper function for drawing a regular polygon with a
specified number of sides and side length. It then creates a turtle and draws
a 7-sided polygon as an example.
"""

import turtle

def pylogon(t, n, length):
    """Draw a regular polygon with the given turtle.

    Parameters:
        t (turtle.Turtle): The turtle used to draw the polygon.
        n (int): The number of sides of the polygon.
        length (int | float): The length of each side.

    Example:
        >>> import turtle
        >>> screen = turtle.Screen()
        >>> bob = turtle.Turtle()
        >>> pylogon(bob, 4, 50)
    """
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


turtle.speed(10)
t = turtle.Turtle()
pylogon(t, 7, 70)
turtle.mainloop()

