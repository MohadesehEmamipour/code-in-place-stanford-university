"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random 
min_random=random.randint(10,99)

max_random=random.randint(10,99)


def main():
    print('What is',min_random,'+',max_random,'?')
    a=int(input('Your answer:'))
    c=min_random+max_random
    if a==c:
        print('Correct!')
    else:
        print('Incorrect. The expected answer is',c)

if __name__ == '__main__':
    main()
