#!/usr/bin/env python3
import prompt
import operator

from random import randint, choice
from math import gcd

# Functions which using game with type 'calc'.
operator_functions = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}

# Define the limits for the brain games questions.
# randint(left_limit, right_limit) - range for random numbers.
left_limit, right_limit = 1, 20

# Progression properties (minimum and maximum lenght.)
minimum_lenght, maximum_lenght = 5, 10


def games(game_type, name):
    game_flag = True
    win_counter = 0
    while game_flag:
        question, correct_answer = questions_and_answers(game_type)
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')
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


def questions_and_answers(game_type):
    if game_type == 'even':
        question = randint(left_limit, right_limit)
        if question % 2 == 0:
            correct_answer = 'yes'
        elif question % 2 != 0:
            correct_answer = 'no'
    elif game_type == 'calc':
        a = randint(left_limit, right_limit)
        b = randint(left_limit, right_limit)
        ab = choice(list(operator_functions))
        question = str(a) + ' ' + str(ab) + ' ' + str(b)
        correct_answer = str(operator_functions[ab](a, b))
    elif game_type == 'gcd':
        a = randint(left_limit, right_limit)
        b = randint(left_limit, right_limit)
        question = str(a) + ' ' + str(b)
        correct_answer = str(gcd(a, b))
    elif game_type == 'prog':
        step = randint(left_limit, right_limit)
        lenght = randint(minimum_lenght, maximum_lenght)
        starting_number = randint(left_limit, right_limit)
        secret_index = randint(0, lenght - 1)
        question = ''
        for i in range(lenght):
            if i != secret_index:
                question += str(starting_number + i * step) + ' '
            elif i == secret_index:
                question += '.. '
                correct_answer = str(starting_number + i * step)
        question.rstrip()
    return question, correct_answer
