"""
TODO: Write a description here
"""

def main():
    stone=20
    print('There are 20 stones left')
    while stone>0:
        a=input('Player 1 would you like to remove 1 or 2 stones? ')
        s=int(a)
        if s==1:
            stone=stone-1
            print('There are',stone,'stones left')
            if stone==2:
                if s==2:
                    print('Player 2 wins!')
            
                elif b==2:
                    print('Player 1 wins!')
            if stone==1 :
                if s==1:
                    print('Player 2 wins!')
            
                elif b==1:
                    print('Player 1 wins!')
            
        if s==2:
            stone=stone-2
            print('There are',stone,'stones left')
            if stone==2:
                if s==2:
                    print('Player 2 wins!')
            
                elif b==2:
                    print('Player 1 wins!')
            if stone==1 :
                if s==1:
                    print('Player 2 wins!')
            
                elif b==1:
                    print('Player 1 wins!')
            
        two=input('Player 2 would you like to remove 1 or 2 stones? ')
        b=int(two)
        if b==1:
            stone=stone-1
            print('There are',stone,'stones left')
            if stone==2:
                if s==2:
                    print('Player 2 wins!')
            
                elif b==2:
                    print('Player 1 wins!')
            if stone==1 :
                if s==1:
                    print('Player 2 wins!')
            
                elif b==1:
                    print('Player 1 wins!')
        if b==2:
            stone=stone-2
            print('There are',stone,'stones left')
            if stone==2:
                if s==2:
                    print('Player 2 wins!')
            
                elif b==2:
                    print('Player 1 wins!')
            if stone==1 :
                if s==1:
                    print('Player 2 wins!')
            
                elif b==1:
                    print('Player 1 wins!')



if __name__ == '__main__':
    main()
