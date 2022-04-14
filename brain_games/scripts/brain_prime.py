#!/usr/bin/env python
"""Brain prime main package."""
import prompt
from brain_games.gen_func import is_prime, welcome_user, wrong_message


def main():
    """Brain prime main function."""
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    count = 0

    while True:
        correct = is_prime()
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
