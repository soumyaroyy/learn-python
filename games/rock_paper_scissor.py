import random

ROCK = 'r'
SCISSORS = 's'
PAPPER = 'p'
emojis = {ROCK: '🪨', ROCK: '✄', PAPPER: '🔖'} #object collection
choices = tuple(emojis.keys())

def get_user_chose():
    while True:
        user_choice = input('Rokc, Paper, or scissors? (r/p/s): ').lower()
        if user_choice  in choices:
            return user_choice
        else:
            print('Invalid choice!')

def display_choises(user_choice, computer_choice):            
    print(f'Your Chose {emojis[user_choice]}')
    print(f'Computer Chose {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice :
        print('Tie!')
    elif (
        (user_choice == ROCK and computer_choice == ROCK) or 
        (user_choice == ROCK and computer_choice == PAPPER) or 
        (user_choice == PAPPER and computer_choice == ROCK) ):
        print('You Win!')
    else:
        print('Your lose')


def play_game():
    while True:
        user_choice = get_user_chose()

        computer_choice = random.choice(choices)

        display_choises(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)
    

        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
            break

play_game()

