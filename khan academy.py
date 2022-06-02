"""
TODO: Write a description here
"""
import random
min_random=random.randint(10,99)
max_random=random.randint(10,99)
d=0
d =d+1
def main():
    min_random=random.randint(10,99)
    max_random=random.randint(10,99)
    while (min_random,max_random)!="" :
        min_random=random.randint(10,99)
        max_random=random.randint(10,99)
        print('What is',min_random,'+',max_random,'?')
        a=int(input('Your answer:'))
        c=min_random+max_random
        d=0
        d =d+1
        if a==c:
            d=0
            d =d+1
            print("Correct! You've gotten",d,"correct in a row.")
            d=0
            d =d+1
            if d>=3:
                d=0
                d =d+1
                print('Congratulations! You mastered addition.')
        else:
            print('Incorrect. The expected answer is',c)
            


if __name__ == '__main__':
    main()
