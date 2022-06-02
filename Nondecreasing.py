
def main():
    # TODO write your solution here
    pass
    print('Enter a sequence of non-decreasing numbers.')
    a1=float(input('Enter num: '))
    a2=float(input('Enter num: '))
    d=a2-a1
    n=a1+(n-1)*d
    while a2>a1:
        a2=float(input('Enter num: '))
        d=a2-a1
        n=a1+(n-1)*d
        if a2<a1:
            break

    if a2<a1:
        d=a2-a1
        n=a1+(n-1)*d
        
        print('Thanks for playing!')
        print('Sequence length: ',n)


if __name__ == "__main__":
    main()
