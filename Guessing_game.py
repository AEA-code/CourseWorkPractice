import random
secret_number = random.randint(1,100)
attempt = 0
print('Welcome to the number guessing game')
print('I am thinking of the number between 1 and 100')
while True:
    guess = int(input('Take a guess'))
    attempt += 1

    if guess == secret_number:
        print(f'Congratulation you have guess the {attempt} attempt.')
    elif guess < secret_number:
        print('Too low!, Try  again')
    else:
        print('Too high!, Try again')