'''
    1 for snake
    -1 for water
    0 for gun
'''

computer = -1
you  = input("Enter your choice: ")
youDict = {'snake':1, 'water':-1, 'gun':0}
younum = youDict[you]

if (computer == -1 and you ==1):
    print("You win!")
elif (computer == 1 and you ==0):
    print("You Lose!")
elif (computer == 0 and you ==-1):
    print("You win!")
elif (computer == 0 and you ==1):
    print("You Lose!")
elif (computer == 1 and you ==-1):
    print("You Lose!")
elif (computer == -1 and you ==0):
    print("You win!")
else:
    print("It's a tie!")
'''
    1 for snake
    -1 for water
    0 for gun
'''