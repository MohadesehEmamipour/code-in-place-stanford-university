from TextGrid import TextGrid

DEFAULT_FILENAME = 'guava.txt'

def main():
    grid = TextGrid(DEFAULT_FILENAME)
    letter_A_seen = False # boolean value which will serve as a switch

    for y in range(grid.height):
        for x in range(grid.width):
            cell = grid.get_cell(x, y)
            if cell.value == 'A':
                letter_A_seen = True # flip the switch!
            if letter_A_seen:
                cell.value = 'A'
    print(grid)

if __name__ == '__main__':
    main()
