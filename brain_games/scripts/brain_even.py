#!/usr/bin/env python
"""Brain even main package."""
import prompt
from brain_games.gen_func import is_even, welcome_user, wrong_message


def main():
    """Brain even main function."""
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 0

    while True:
        correct = is_even()
        answer = prompt.string('Your answer: ')

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
