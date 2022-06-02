def main():
    # TODO write your solution here
    pass
    a=float(input('Enter your height in meters:'))
    if 1.6<a<1.9:
        print('Correct height to be an astronaut')
    elif a<1.6:
        print('Below minimum astronaut height')
    elif a>1.9:
        print('Above maximum astronaut height')

if __name__ == "__main__:
    main()
