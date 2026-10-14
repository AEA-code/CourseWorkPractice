import random
choice = ["rock", "paper", "scissors"]

while True:
    user_choice = input('Enter rock, paper or scissors: ').lower()
    if user_choice not in choice:
        print('Invalid choice. Please enter rock, paper, or scissor.')
        continue

    computer_choice = random.choice(choice)
    print(f'user_choice is {user_choice}')
    print(f'computer_choice is {computer_choice}')

    if user_choice == computer_choice:
        print('It is tie')
    elif user_choice == "rock" and computer_choice == "scissors":
        print('You win! rock smashes scissor')
    elif user_choice == "paper" and computer_choice == "rock":
        print('You win! paper covers the rock')
    elif user_choice == "scissors" and computer_choice == "paper":
        print('You win! scissors cuts paper')
    else:
        print("Computer wins! Better luck next time")

    play_again = input('Play again? (y/n): ').lower()
    if play_again not in ('y', 'yes'):
        break
