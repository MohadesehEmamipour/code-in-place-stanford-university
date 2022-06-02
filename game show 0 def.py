def main(): 
    print("Welcome to the CodeInPlace Game Show")
    print("Pick a door and win a prize")
    print("------------------------------------")
    a=one_door()
    p=other_door(a)
    print('you win '+str(p),'stuff')

def one_door():
    a=int(input('Door:'))
    while a<1 or a>3:
        print('Invalid door')
        a=int(input('Door:'))
    
def other_door(a):
    prize=4
    if a==1:
        prize=4*9//10
    elif a==2:
        locked=prize % 2 != 0
        if not locked:
            prize +=10
    elif a==3:
        for i in range(a):
            prize=prize+i
    return prize


if __name__ == '__main__':
    main()

