#!/usr/bin/env python3
import prompt
import operator

from random import randint, choice
from math import gcd, sqrt

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

# Prime number properties (maximum number).
maximum_number = 100


def games(game_type, name):
    game_flag = True
    win_counter = 0
    while game_flag:
        question, correct_answer = select_game(game_type)
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


def select_game(game_type):
    if game_type == 'even':
        question, correct_answer = even_game()
    elif game_type == 'calc':
        question, correct_answer = calc_game()
    elif game_type == 'gcd':
        question, correct_answer = gcd_game()
    elif game_type == 'prog':
        question, correct_answer = prog_game()
    elif game_type == 'prime':
        question, correct_answer = prime_game()
    return question, correct_answer


def even_game():
    question = randint(left_limit, right_limit)
    if question % 2 == 0:
        correct_answer = 'yes'
    elif question % 2 != 0:
        correct_answer = 'no'
    return question, correct_answer


def calc_game():
    a = randint(left_limit, right_limit)
    b = randint(left_limit, right_limit)
    ab = choice(list(operator_functions))
    question = str(a) + ' ' + str(ab) + ' ' + str(b)
    correct_answer = str(operator_functions[ab](a, b))
    return question, correct_answer


def gcd_game():
    a = randint(left_limit, right_limit)
    b = randint(left_limit, right_limit)
    question = str(a) + ' ' + str(b)
    correct_answer = str(gcd(a, b))
    return question, correct_answer


def prog_game():
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


def prime_game():
    question = randint(1, maximum_number)
    if question == 1:
        correct_answer = 'yes'
    else:
        for i in range(2, int(sqrt(question)) + 1):
            if question % i == 0:
                correct_answer = 'no'
                break
            correct_answer = 'yes'
    return question, correct_answer
