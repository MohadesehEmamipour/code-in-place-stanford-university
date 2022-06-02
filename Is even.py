def is_even(num):
    if num % 2 == 0:
        # num is even!
        return True
    # Since returning ends the function execution,
    # the below return statement will execute only if the number is not even.
    # We could've also put it in an else statement -- 
    # can you convince yourself why this does the same thing?
    return False

def main():
    num = int(input("Enter a number: "))
    if is_even(num):
        print("That number is even!")
    else:
        print("That number is not even!")

if __name__ == "__main__":
    main()
