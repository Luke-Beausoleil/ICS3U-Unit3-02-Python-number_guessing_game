#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: April 2021
# This program lets the user play a number guessing game

import constants


def main():
    # this function gets user to guess a number and tells them if it's correct

    # input
    guess = int(input("Guess a number from 0 - 9: "))

    # process & output
    if guess < constants.CORRECT_NUMBER:
        print("\nToo Low, Try Again!")
    if guess == constants.CORRECT_NUMBER:
        print("\nCorrect!")
    if guess > constants.CORRECT_NUMBER:
        print("\nToo High, Try Again!")
    if abs(guess - constants.CORRECT_NUMBER) == constants.SMALL_DIFFERENCE:
        print("You're Very Close!")
    # learned absolute value from https://www.guru99.com/abs-in-python.html#:~
    #   :text=Abs()%20is%20a%20built%2Din%20function%20available%20with%20
    #   python,want%20to%20get%20the%20absolute.
    print("\nDone.")


if __name__ == "__main__":
    main()
