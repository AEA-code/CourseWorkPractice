
"""Organized Python Practice Work.
Run this file and select an exercise number. Only the selected exercise runs.
Examples use illustrative values from the original notes.
"""
import math
import os
import random
import statistics
from datetime import date, datetime
from pathlib import Path


def exercise_01():
    """Basic input, conditions, and games."""
    choice = 9
    guess = int(input('Guess a number from 1 to 10: '))
    print('You win!' if guess == choice else 'Sorry, you lose!')


def exercise_02():
    """Guessing game with input validation."""
    choice = 7
    while True:
        try:
            guess = int(input('Enter a number between 1 and 10: '))
            if 1 <= guess <= 10:
                break
            print('Enter a number between 1 and 10.')
        except ValueError:
            print('Please enter a valid integer.')
    print('You win!' if guess == choice else 'Sorry, you lose!')


def exercise_03():
    """Rock-paper-scissors."""
    computer_choice = 'paper'
    player_choice = input('Rock, paper, or scissors: ').strip().lower()
    valid_choices = ('rock', 'paper', 'scissors')
    if player_choice not in valid_choices:
        print('Invalid choice.')
    elif player_choice == computer_choice:
        print("It's a tie!")
    elif ((player_choice == 'rock' and computer_choice == 'scissors') or
          (player_choice == 'paper' and computer_choice == 'rock') or
          (player_choice == 'scissors' and computer_choice == 'paper')):
        print('Congratulations! You won!')
    else:
        print('The computer wins.')


def exercise_04():
    """Variables, types, conversions, and strings."""
    z = 1.2
    print('Is float?', isinstance(z, float))
    number = int('23')
    print('Converted number:', number)
    name = 'elolo'
    print(name.capitalize(), name.upper(), name.splitlines())
    print('First o in Hello World:', 'Hello World'.find('o'))


def exercise_05():
    """Arithmetic, assignments, and Boolean expressions."""
    if 3**2 + 4**2 == 5**2:
        print('3, 4, 5 form a right triangle')
    elif 3**2 < 4**2:
        print('34')
    else:
        print('5')
    a, b, c = 12.3, 100, 0
    if a < b:
        a += 1
        b -= 1
        c -= b
    print('a =', a, 'c =', c)
    a, b, c = 100, 200, 300
    ab, cd = a < b, c == a + b
    if ab and cd:
        print('AB and CD')
    elif ab:
        print('AB')
    else:
        print('Nope')
    minutes = 24
    minutes -= 4
    minutes += 1.1
    print('Minutes:', minutes)


def exercise_06():
    """Comparing strings and numeric strings."""
    print('toast' if 'toast' < 'jam' else 'jam')
    print('12' if '12' < '15' else '5')
    print('Numeric comparison:', int('12') < int('15'))


def exercise_07():
    """For and while loops, powers, and fractions."""
    a = 0
    while a < 10:
        a += 1
    print('Counter:', a)
    for i in range(65):
        print(i, 2**i)
    print('2**64 * 2**64:', 2**64 * 2**64)
    count, n, value = 1, 1, 4
    while count < 16:
        print(value / n)
        count += 1
        n += 2
    total = 0
    for term in range(1, 21):
        total += 1 / (2**term)
    print('First fraction series:', total)
    total = 0
    for n in range(2, 32, 2):
        total += 2 / (2**n)
    print('Second fraction series:', total)
    i = 0
    while i < 10:
        result = i * 2
        i += 1
    print('Last result and i:', result, i)


def newton(f, dfdx, guess, max_iter=20, tol=1e-3):
    """Approximate a root of f(x)=0 using Newton's method."""
    iteration = 0
    while iteration < max_iter:
        f_value = f(guess)
        if abs(f_value) <= tol:
            return True, iteration, guess
        derivative = dfdx(guess)
        if derivative == 0:
            return False, iteration, guess
        guess = guess - f_value / derivative
        iteration += 1
    return abs(f(guess)) <= tol, iteration, guess


def exercise_08():
    """Functions: Newton's method for the square root of 2."""
    def f(x):
        return x**2 - 2
    def dfdx(x):
        return 2 * x
    success, iterations, root = newton(f, dfdx, 1.0)
    print('Converged:', success)
    print('Iterations:', iterations)
    print('Approximate root:', root)


def exercise_09():
    """Lists, tuples, intersections, and perfect squares."""
    numbers = [1, 2, 4, 7, 12, 15, 21]
    for number in numbers:
        print(number, number * 2)
    # Prefer a direct loop to exec() when the code is already known.
    atoms = ('Hydrogen', 1, 'Helium', 2, 'Lithium', 3,
             'Beryllium', 4, 'Boron', 5, 'Carbon', 6)
    for i in range(0, len(atoms), 2):
        element, protons = atoms[i], atoms[i + 1]
        print(f'{element}: protons={protons}, twice protons={protons * 2}')
    a = [1, 2, 3, 4, 5, 6]
    b = [2, 4, 6, 8, 10, 12]
    common_total = 0
    for item in a:
        if item in b:
            common_total += item
    print('Sum of common elements:', common_total)
    even_numbers = tuple(range(2, 101, 2))
    squares = [n for n in even_numbers if math.isqrt(n)**2 == n]
    print('Even perfect squares:', squares)


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, math.isqrt(number) + 1):
        if number % divisor == 0:
            return False
    return True


def exercise_10():
    """Prime-number guessing quiz."""
    number = random.randint(10_000, 1_000_000)
    answer = input(f'Is {number} prime? True or False: ').strip().lower()
    if answer in ('true', 't', 'yes', 'y', '1'):
        user_thinks_prime = True
    elif answer in ('false', 'f', 'no', 'n', '0'):
        user_thinks_prime = False
    else:
        user_thinks_prime = None
    actual_answer = is_prime(number)
    if user_thinks_prime is None:
        print('Invalid answer. Enter True or False.')
    elif user_thinks_prime == actual_answer:
        print('You are correct!')
    else:
        print('Not correct.')
    print('Actual answer:', actual_answer)


def exercise_11():
    """Counting divisors and finding the number with most divisors below 1000."""
    k = 100
    count = 0
    for divisor in range(1, k + 1):
        if k % divisor == 0:
            count += 1
    print(f'{k} has {count} positive divisors.')
    max_value, max_count = 1, 0
    for k in range(1, 1000):
        count = 0
        for divisor in range(1, k + 1):
            if k % divisor == 0:
                count += 1
        if count > max_count:
            max_count, max_value = count, k
    print(f'Most divisors: {max_value}, with {max_count} divisors.')


def exercise_12():
    """Text-based bar chart using hash symbols."""
    quarters = {'Q1': 190000, 'Q2': 340000, 'Q3': 87300, 'Q4': 439833}
    for quarter, value in quarters.items():
        print(f'{quarter}: {"#" * (value // 20000)} {value}')


def exercise_13():
    """Celsius to Fahrenheit conversion."""
    celsius = float(input('Temperature in Celsius: '))
    fahrenheit = celsius * 9 / 5 + 32
    print(f'Fahrenheit equivalent: {fahrenheit:.2f}°F')


def exercise_14():
    """Working directories and creating nested directories."""
    print('Current working directory:', os.getcwd())
    os.makedirs('College/Python/Programs', exist_ok=True)
    print('Directory contents:', os.listdir())


def exercise_15():
    """Write, read, count, append, and read a file line by line."""
    file_path = Path('Myfile.txt')
    all_text = ('My first file-writing practice.\n'
                'My second file-writing practice.\n'
                'My third file-writing practice was amazing.\n')
    # 'w' overwrites an existing file of the same name.
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(all_text)
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.read()
    print(contents)
    with open(file_path, 'r', encoding='utf-8') as file:
        word_count = len(file.read().split())
    print('Number of words:', word_count)
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write('\nThis is appended text.')
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')


def exercise_16():
    """Delete only the practice file, after confirmation."""
    file_path = Path('Myfile.txt')
    if not file_path.exists():
        print('File does not exist.')
        return
    if input('Delete Myfile.txt? Type YES to confirm: ') == 'YES':
        file_path.unlink()
        print('File deleted.')
    else:
        print('Deletion cancelled.')


class Player:
    score = 5

    def cal_player(self, score):
        return self.score + score


class BasicCar:
    wheel = 4

    def drive_to(self, town):
        print(f'The car drives to {town} on {self.wheel} wheels.')

    def number_of_wheels(self):
        print(f'The car has {self.wheel} wheels.')


class Car:
    wheel = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def destination(self, location):
        return f'The {self.color} {self.brand} is driving to {location}.'

    def number_of_wheels(self):
        return f'The {self.color} {self.brand} has {self.wheel} wheels.'


def exercise_17():
    """OOP: class attributes, instance methods, and constructors."""
    player = Player()
    print(player.cal_player(23))
    basic_car = BasicCar()
    basic_car.drive_to('Accra')
    basic_car.number_of_wheels()
    car = Car('Toyota', 'Red')
    print(car.destination('Dubai'))
    print(car.number_of_wheels())


class Task:
    """Task with a validated date property and rescheduling method."""
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.status = 'Pending'

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        if not isinstance(value, date) or isinstance(value, datetime):
            raise TypeError('due_date must be a date object.')
        self._due_date = value

    def reschedule(self, new_date):
        self.due_date = new_date


def exercise_18():
    """OOP: properties, validation, and task rescheduling."""
    task = Task('Study Python', date(2026, 11, 1))
    print(task.name, task.due_date, task.status)
    task.reschedule(date(2026, 11, 2))
    print('Rescheduled due date:', task.due_date)


def exercise_19():
    """Standard-library practice: datetime, statistics, and math."""
    print('Current date and time:', datetime.now())
    print('Sample standard deviation:', statistics.stdev([1, 2, 3, 4, 5]))
    print('Integer square root of 100:', math.isqrt(100))


EXERCISES = {
    '1': ('Number guessing', exercise_01),
    '2': ('Number guessing with validation', exercise_02),
    '3': ('Rock-paper-scissors', exercise_03),
    '4': ('Variables, types, and strings', exercise_04),
    '5': ('Arithmetic and Boolean expressions', exercise_05),
    '6': ('Comparing strings', exercise_06),
    '7': ('Loops and fraction sequences', exercise_07),
    '8': ("Newton's method", exercise_08),
    '9': ('Lists and tuples', exercise_09),
    '10': ('Prime number quiz', exercise_10),
    '11': ('Counting divisors', exercise_11),
    '12': ('Text-based bar chart', exercise_12),
    '13': ('Temperature conversion', exercise_13),
    '14': ('Working with directories', exercise_14),
    '15': ('Writing and reading files', exercise_15),
    '16': ('Deleting the practice file', exercise_16),
    '17': ('OOP: Player and Car', exercise_17),
    '18': ('OOP: Task and properties', exercise_18),
    '19': ('Datetime, statistics, and math', exercise_19),
}

if __name__ == '__main__':
    print('PYTHON PRACTICE WORK — SELECT AN EXERCISE')
    for number, (title, _) in EXERCISES.items():
        print(f'{number:>2}. {title}')
    selected = input('Enter exercise number (or press Enter to exit): ').strip()
    if selected in EXERCISES:
        print('\n---', EXERCISES[selected][0], '---')
        EXERCISES[selected][1]()
    elif selected:
        print('Invalid exercise number.')

# NOTES
# File modes: r=read, w=write/overwrite, a=append, x=create if absent.
# Use with open(...) for safe file handling; \n inserts a newline.
# Operators: ** exponentiation, % remainder; range(start, stop, step).
# Shift+Alt+Down duplicates a line in some editors.
