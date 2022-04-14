#!/usr/bin/env python
"""Brain even main package."""
from random import randint

import prompt


def is_even(number):
    """
    Check is even number function.

    Args:
        number: number for check

    Returns:
        str
    """
    if number % 2 == 0:
        return 'yes'

    return 'no'


def welcome_and_start():
    """
    Welcome and start game function.

    Returns:
        str
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name


def question():
    """
    Generate question function.

    Returns:
        dict
    """
    number = randint(0, 100)
    correct = is_even(number)
    print('Question: {0}'.format(number))
    answer = prompt.string('Your answer: ')
    return {
        'answer': answer,
        'correct': correct,
    }


def main():
    """Brain games main function."""
    name = welcome_and_start()
    count = 0
    is_true = True

    while is_true:
        res = question()

        if res['answer'] == res['correct']:
            print('Correct!')
            count += 1
        else:
            is_true = False
            print("'{0}' is wrong answer ;(.".format(res['answer']), end=' ')
            print("Correct answer was '{0}'.".format(res['correct']))
            print("Let's try again, {0}!".format(name))

        if count >= 3:
            is_true = False
            print('Congratulations, {0}!'.format(name))


if __name__ == '__main__':
    main()
