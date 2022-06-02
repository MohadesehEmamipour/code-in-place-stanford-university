"""
TODO: Write a description here
"""

import random
n_stones=20

def main():
    n_stones=20
    print('There are',n_stones,'stones left')
    while n_stones>0:
        player_one=int(input('Player 1 would you like to remove 1 or 2 stones?'))
        amount()
        player_two=int(input('Player 2 would you like to remove 1 or 2 stones?'))
        amount()

def amount():
    remove=random.randint(1,2)
    n_stones=20
    turn=1
    while n_stones>0:
        
        if player_one==1 :
            n_stones=n_stones-1
            print('There are',n_stones,'stones left')
        elif player_one==2 :
            n_stones=n_stones-2
            print('There are',n_stones,'stones left')
        else:
            print('Game over')
            
            
        

if __name__ == '__main__':
    main()
