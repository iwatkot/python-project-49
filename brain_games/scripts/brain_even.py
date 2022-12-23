#!/usr/bin/env python3
import prompt

from random import randint

from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_flag = True
    win_counter = 0
    while game_flag:
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            correct_answer = 'yes'
        elif number % 2 != 0:
            correct_answer = 'no'
        if answer == correct_answer:
            print('Correct!')
            win_counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            game_flag = False
        if win_counter == 3:
            print(f"Congratulations, {name}!")
            game_flag = False


if __name__ == '__main__':
    main()
