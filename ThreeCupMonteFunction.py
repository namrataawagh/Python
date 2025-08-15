# Python Functions to mimic carnival guessing game "Three Cup Monte"
from random import shuffle

def shuffle_list(my_list):
    shuffle(my_list)
    return my_list


def player_guess():

    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0 , 1 , 2:")

    return int(guess)



def game(my_list,guess):
    if my_list[guess] == 'O':
        print('Correct')
    else:
        print('Try again!')
        print(my_list)

# 1. INITIAL LIST
my_list = [' ','O',' ']

# 2. SHUFFLE LIST
mixedup_list = shuffle_list(my_list)

# 3. USER GUESS
guess = player_guess()

# 4. CHECK GUESS
game(mixedup_list,guess)