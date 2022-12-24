#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.games.all_games import games


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    games('prog', name)


if __name__ == '__main__':
    main()
