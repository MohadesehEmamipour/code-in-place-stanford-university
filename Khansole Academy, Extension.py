"""
TODO: Write a description here
"""
import random
min_random=random.randint(10,99)
max_random=random.randint(10,99)
answer_pass=3

def main():
    min_random=random.randint(10,99)
    max_random=random.randint(10,99)
    correct=0
    while correct<answer_pass :
        min_random=random.randint(10,99)
        max_random=random.randint(10,99)
        print('What is',min_random,'+',max_random,'?')
        a=int(input('Your answer:'))
        c=min_random+max_random
        
        if a==c:
            correct +=1
            print("Correct! You've gotten",correct,"correct in a row.")
            if a==c and correct==3:
                print('Congratulations! You mastered addition.')
        else:
            correct=0
            print('Incorrect. The expected answer is',c)
if __name__ == '__main__':
    main()
