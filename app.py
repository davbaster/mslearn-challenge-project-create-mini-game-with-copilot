'''
Write a rock, paper, scissors game. the player can choose one of the three options, and should be warned if they enter an invalid option. At each round, the player must enter
one of the options and be informed if the won, lost, or tied with the opponent. By the end of each round, the player can choose whether to play again or not. 
the game must handle user inputs, putting them in lower case and informing the user if the option is valid or invalid.
Display the player's score at the end of the game.
'''

import random

print('Welcome to Rock, Paper, Scissors game!')
print('What is your name?')
name = input()
print('Hello ' + name + '!')

while True:
    print('Please choose your option: (r)ock, (p)aper, (s)cissors')
    user_input = input()
    user_input = user_input.lower()

    if user_input == 'r':
        user_input = 'rock'
    elif user_input == 'p':
        user_input = 'paper'
    elif user_input == 's':
        user_input = 'scissors'
    else:
        print('Invalid option! Please choose again.')
        continue

    print('Your option is ' + user_input + '.')

    options = ['rock', 'paper', 'scissors']
    computer_input = random.choice(options)
    print('The computer chose ' + computer_input + '.')

    if user_input == computer_input:
        print('It is a tie!')
    elif user_input == 'rock' and computer_input == 'scissors':
        print('You won!')
    elif user_input == 'paper' and computer_input == 'rock':
        print('You won!')
    elif user_input == 'scissors' and computer_input == 'paper':
        print('You won!')
    else:
        print('You lost!')

    print('Do you want to play again? (y)es or (n)o')
    user_input = input()
    user_input = user_input.lower()

    if user_input == 'y':
        continue
    else:
        break

