"""
Prints out 10 random numbers between 0 and 100.
"""

import random
NUM_RANDOM=random.randint(0,100)
MIN_RANDOM=0
MAX_RANDOM=100
NUM_RANDOM=10
def main():
    for NUM_RANDOM in range(10):
        print(NUM_RANDOM)

if __name__ == '__main__':
    main()
