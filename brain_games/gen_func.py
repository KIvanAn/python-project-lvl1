"""General functions for brain games package."""
import math
from random import choice, randint

import prompt


def is_even():
    """
    Check is even number function.

    Returns:
        str
    """
    number = randint(0, 100)
    print('Question: {0}'.format(number))

    if number % 2 == 0:
        return 'yes'

    return 'no'


def welcome_user():
    """
    Welcome and return user's name function.

    Returns:
        str
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def wrong_message(answer, correct, user):
    """
    Print wrong message answer function.

    Args:
        answer: user's answer
        correct: correct answer
        user: user's name
    """
    print("'{0}' is wrong answer ;(.".format(answer), end=' ')
    print("Correct answer was '{0}'.".format(correct))
    print("Let's try again, {0}!".format(user))


def calculate():
    """
    Calculate function.

    Returns:
        int
    """
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    operation = choice(['-', '+', '*'])

    print('Question: {0} {1} {2}'.format(number1, operation, number2))

    if operation == '-':
        return number1 - number2
    elif operation == '+':
        return number1 + number2
    elif operation == '*':
        return number1 * number2


def find_gcd():
    """
    GCD function.

    Returns:
        int
    """
    number1 = randint(0, 100)
    number2 = randint(0, 100)

    print('Question: {0} {1}'.format(number1, number2))

    return math.gcd(number1, number2)


def get_progression():
    """
    Progression function.

    Returns:
        int
    """
    step = randint(1, 5)
    index = randint(0, 9)
    acc = 0
    progres = []
    for _ in range(10):
        acc += step
        progres.append(str(acc))

    secret_num = int(progres[index])
    progres[index] = '..'

    print('Question: {0}'.format(' '.join(progres)))

    return secret_num
