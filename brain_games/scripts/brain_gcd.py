#!/usr/bin/env python
"""Brain gcd main package."""
import prompt
from brain_games.gen_func import find_gcd, welcome_user, wrong_message


def main():
    """Brain gcd main function."""
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')

    count = 0

    while True:
        correct = find_gcd()
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
