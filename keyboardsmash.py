import random
from TextGrid import TextGrid

SMASHABLE_LETTERS = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';']
NUM_LETTERS = 10

def main():
    grid = TextGrid.blank(NUM_LETTERS, 1)
    
    for x in range(grid.width):
        random_value = get_random_value()
        cell = grid.get_cell(x, 0)
        cell.value = random_value
    
    print(grid)

def get_random_value():
    idx = random.randint(0,len(SMASHABLE_LETTERS) - 1) # randomly generate an index
    return SMASHABLE_LETTERS[idx] # return alphabetic letter

if __name__ == '__main__':
    main()
