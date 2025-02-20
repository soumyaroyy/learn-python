#AskL roll the dice? 
#if user enters y 
#   Generate two rendom numbers
#   Print them
# If user enters n
#   Print tank you message
#   Terminate
# Else 
#   Print invalid choice
import random

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        die1 = random.randint(1, 9)
        die2 = random.randint(1, 9)
        print(f'({die1}, {die2})')

    elif choice == 'n':
        print('Thank for playing!')
        break
    else:
        print('Invalid choice!')