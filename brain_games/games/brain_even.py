#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.games.all_games import games


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    games('even', name)


if __name__ == '__main__':
    main()
