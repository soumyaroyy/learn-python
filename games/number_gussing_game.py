# Guess the number ( between 1 and 100):
# seleted number 5
#if user enters num > 5
#   Print Too high! try again
#   Terminate
#If user enters num < 5
#   Print Too low! Try again
#   Terminate
# If user enters num == 5 
#   Congratulations! You gussed the number in 5 attempts
import random

number_to_guess = random.randint(1, 100)
while True:
    try: 
        guess = int(input("Guess the number ( between 1 and 100): "))
        if guess == number_to_guess:
            print('Congratulations! You gussed the number.')
            break
        elif guess < number_to_guess:
            print('Too low! Try again')
        else :
            print('Too high! try again')
    except ValueError:
        print('Please Enter a valid number')


