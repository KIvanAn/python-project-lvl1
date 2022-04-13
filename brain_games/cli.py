"""Return the cli functions."""
import prompt


def welcome_user():
    """Show welcome message for user."""
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
