#!/usr/bin/env python
"""Brain games main package."""
from brain_games.cli import welcome_user


def main():
    """Brain games main function."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
