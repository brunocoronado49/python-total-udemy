from random import *

def find_the_number():
    lives = 8
    player_number = 0
    correct_number = randint(1, 100)
    
    print('Welcome to find the number!')
    
    while lives > 0:
        player_number = int(input('Please enter a number (0 - 99): '))
        lives -= 1
        print(f'Lives: {lives}')
        
        if player_number > correct_number:
            print('Number bigger than the correct')
        elif player_number < correct_number:
            print('Number lower than correct number')
        elif player_number > 100:
            print('Your number are so bigger, try again')
        else:
            print(f'Congratulations!!! You Win! the number was {correct_number}')
            break
        
    if lives == 0:
        print('You are dead!')
    
    
    

find_the_number()