"""
Prints the Fizz Buzz sequence up to a given number.
"""
fizz=3
buzz=5
def main():
    a=input('Number to count to:')
    limit=int(a)
    fizz_num=0
    buzz_num=0
    fizzbuzz_num=0
    for i in range(1,limit+1):
        if i % fizz == 0 and i % buzz == 0 :
            fizzbuzz_num =+ 1
            print('Fizzbuzz')
        elif i % fizz == 0 :
            fizz_num +=1
            print('Fizz')
        elif i % buzz == 0 :
            buzz_num +=1
            print('Buzz')
        
        else:
            print(i)
    print('')
    print('Num fizzed:',fizz_num)
    print('Num buzzed:',buzz_num)
    print('Num fizzbuzzed:',fizzbuzz_num)
if __name__ == '__main__':
    main()
