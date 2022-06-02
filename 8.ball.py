"""
Simulates a magic eight ball.
Prompts the user to type a yes or no question and gives
a random answer from a set of prefabricated responses.
"""

import random

ANSWER_1 = "Yes."
ANSWER_2 = "Not a chance."
ANSWER_3 = "Only Karel knows."
ANSWER_4 = "Without a doubt."
ANSWER_5 = "Ask again later"

def answer_one_question():
    """
    This function is responsible for answering a question
    using one of the 5 answers defined above. It does this 
    by picking a random number and then printing the corresponding
    answer.

    This code corresponds to milestone 1 of the eight ball problem.
    """
    answer_number = random.randint(1, 5)
    if answer_number == 1:
        print(ANSWER_1)
    if answer_number == 2:
        print(ANSWER_2)
    if answer_number == 3:
        print(ANSWER_3)
    if answer_number == 4:
        print(ANSWER_4)
    if answer_number == 5:
        print(ANSWER_5)

def main():
    """
    This function is responsible for continuously prompting
    the user for a yes or no question until they enter a blank
    question.
    """

    # We need to get the question once from the user 
    # so that we can use it in the loop
    question = input("Ask a yes or no question: ")
    while question != "":
        answer_one_question()
        
        # Get another question from the user
        question = input("Ask a yes or no question: ")

if __name__ == "__main__":
    main()