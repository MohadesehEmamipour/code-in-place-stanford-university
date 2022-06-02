def main():
    print('Welcome to the CodeInPlace Game Show')
    print('Pick a door and win a prize')
    print("----------------------------------------")

    d=int(input('Door:'))
    while d<1 or d>3:
        print('Invalid door')
        d=int(input('Door:'))
    prize=4
    if d==1:
        prize= 2 + 9 // 10 * 100
    elif d==2:
        locked=prize % 2 !=0
        if not locked:
            prize +=6
    elif d==3:
        for i in range(d):
            prize=prize+i

    print('you win '+str(prize)+' stuff')
if __name__ == '__main__':
    main()
