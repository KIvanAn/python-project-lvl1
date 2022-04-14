#!/usr/bin/env python
"""Brain prograssion main package."""
import prompt
from brain_games.gen_func import get_progression, welcome_user, wrong_message


def main():
    """Brain progression main function."""
    name = welcome_user()
    print('What number is missing in the progression?')

    count = 0

    while True:
        correct = get_progression()
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
