#!/usr/bin/env python
"""Brain calc main package."""
import prompt
from brain_games.gen_func import calculate, welcome_user, wrong_message


def main():
    """Brain calc main function."""
    name = welcome_user()
    print('What is the result of the expression?')

    count = 0

    while True:
        correct = calculate()
        answer = int(prompt.string('Your answer: '))

        if answer == correct:
            print('Correct!')
            count += 1
        else:
            wrong_message(answer, correct, name)
            break

        if count >= 3:
            print('Congratulations, {0}!'.format(name))
            break


if __name__ == '__main__':
    main()
