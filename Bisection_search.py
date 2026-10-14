# Using bisection search to find the cube root of a number
cube = int(input('Enter the number you want to find the cube root of:'))
epsilon = 0.01
total_guess = 0
low = 0.0
high = cube
guess = (high + low)/2.0 # guess equal the mid of search
while abs(guess**3 - cube) > epsilon:
    if guess**3 > cube:
        # cube too high
        high = guess
    else:
        low = guess
    guess = (high+low)/2.0
    total_guess += 1
print(f'the total guess is:',total_guess)
print(f'{guess} is near the cubr root of {cube}')
