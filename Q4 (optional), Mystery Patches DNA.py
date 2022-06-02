"""
File: mystery_patches.py
------------------------
This file creates a "mystery" effect on a given DNA TextGrid.
Given a DNA TextGrid, this program creates 4 patches of this DNA TextGrid in row of 4 columns.
The first patch converts all A's to '?', the second patch converts all T's to '?',
the third patch converts all C's to '?', and the fourth patch converts all G's to '?'
"""
import sys
from TextGrid import TextGrid

N_ROWS = 1
N_COLS = 4
PATCH_SIZE = 2
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'patch1.txt'


def edit_patch(to_change):
    """
    Implement this function to edit one patch. This function loads the TextGrid and changes every
    occurrence of the to_change character to a '?'.
    :param to_change: A character that represents the letter to change for this patch (ex. A,T,C,G)
    Returns the newly generated patch
    """

    patch = TextGrid(PATCH_NAME)

    # TODO: your code here

    return patch


def main():
    final_grid = TextGrid.blank(WIDTH, HEIGHT)

    # TODO: your code here
    print(final_grid)

######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) > 0:
        # command line argument to change PATCH_NAME
        PATCH_NAME = args[0]
    main()
