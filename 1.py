import random
min_random=random.randint(10,99)
max_random=random.randint(10,99)

def add_three(x):
    x=x+1
    return x
  
def main():
    min_random=random.randint(10,99)
    max_random=random.randint(10,99)
    x=1
    x=add_three
    while (min_random,max_random)!="" :
        min_random=random.randint(10,99)
        max_random=random.randint(10,99)
        print('What is',min_random,'+',max_random,'?')
        a=int(input('Your answer:'))
        c=min_random+max_random
        x=1
        x=add_three
        if a==c:
            x=1
            x=add_three
            if x==1:
                x=1
                x=add_three
                print('correct',x)
        else:
            print('incorrect',c)
            
                
            
if __name__ == '__main__':
    main()
