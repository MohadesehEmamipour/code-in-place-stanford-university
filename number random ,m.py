"""
Number Guesser Program

This is an example of how to use variables to 
keep track of information in a program that 
also makes use of loops
"""
import random
min_random=0
max_random=100

def main():
    # TODO fill me in!
    num=0
    lowern=min_random
    highern=max_random
    
    while True:
        num +=1
        g=random.randint(lowern,highern)
        
        a=str(input('Is your number '+str(num)+'?'))
        if a=='lower':
            highern=a-1
           
        if a=='higher':
            lowern=a+1
            
        if a=='correct':
            break
    print('I win! It took me'+str(num)+' guesses.')


if __name__ == "__main__":
    main()
