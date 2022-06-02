import random
min_random=random.randint(10,99)
max_random=random.randint(10,99)
while (min_random,max_random)!="" :
    min_random=random.randint(10,99)
    max_random=random.randint(10,99)
    print('What is',min_random,'+',max_random,'?')
    a=int(input('Your answer:'))
    c=min_random+max_random
    #d="You've gotten  correct in a row."
    if a==c:
        print("correct")
        d(3)
    else:
        print("incorrectThe expected answer is ",c)
    
def d(n):
    for d in range(n):
        print("You've gotten",d,"correct in a row.")
    return d
