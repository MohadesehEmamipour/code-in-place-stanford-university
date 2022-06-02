import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'

def get_words():
    list_of_words = []
    with open(FILE_NAME) as f:
        for line in f:
            list_of_words.append(line.strip())
    return list_of_words

def play_game(words):
    while True:
        input(random.choice(words))

def main():
    words = get_words()
    play_game(words)

if __name__ == '__main__':
    main()
