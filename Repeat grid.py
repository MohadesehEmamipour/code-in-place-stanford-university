from TextGrid import TextGrid

DEFAULT_FILENAME = 'abcd.txt'
NUM_REPEATS = 2

def main():
    grid = TextGrid(DEFAULT_FILENAME)
    print("Initial grid:")
    print(grid)
    final_grid = TextGrid.blank(NUM_REPEATS * grid.width, grid.height)
    
    for repeat in range(NUM_REPEATS):
        start_x = grid.width * repeat
        place_grid(grid, final_grid, start_x)

    print("Final grid:")
    print(final_grid)


def place_grid(grid, final_grid, start_x):
    """ Helper function to put letters in `grid` into `final_grid` starting at `start_x` """
    for x in range(grid.width):
        for y in range(grid.height):
            cell = grid.get_cell(x, y)
            final_grid.set_cell(start_x + x, y, cell)


if __name__ == '__main__':
    main()
