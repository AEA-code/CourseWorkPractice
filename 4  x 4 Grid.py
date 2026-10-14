# A 4 by 4 grid
def print_beam():
    print('+' + '----+' * 4)


def print_row():
    print('|' + '    |' * 4)


def print_grid():
    for _ in range(4):
        print_beam()
        for _ in range(1):
            print_row()
    print_beam()


print_grid()

import turtle
bob = turtle.Turtle()
print(bob)
    