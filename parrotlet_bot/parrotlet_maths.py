__author__ = 'Timothy Lam'

import random as r
import math

opp_code = ['/', '+', '*', '-', '^']


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a / b


def multiply(a, b):
    return a * b


def power(a, b):
    return a ** b

def squareroot(a):
    return math.sqrt(a)


def factoria(a):
    return math.factorial(a)


def format_maths_string(string):
    numbers = []
    ops = []
    p = -1
    for i in string:
        if (not i.isnumeric()) and (i != '.') and (i != ' '):
            # print(f"i = {i}")

            if i in ops:
                start = p + 1
                e = string.index(i, start, -1)
                a = string[start:e].strip()
            else:
                e = string.index(i)
                a = string[p + 1:e].strip()
            # print(f"a = {a}")
            b = float(a)
            # print(f"b = {b}")
            numbers.append(b)
            ops.append(i)
            p = e + 0
    numbers.append(float(string.split(ops[-1])[-1]))
    return numbers, ops


def calculate(string):
    response = ["No, you calculate that!",
                "I'm sorry, I am not in the mood for maths",
                "sorry, I forgot my brain at home today",
                "I'm sorry, I have forgotten how to solve that. :(",
                "This looks like a trick question",
                "You are trying to embarrass me with simple arithmetic",
                "Calm down.  I am not google",
                "Hey! Do you think I am some Maths Genius or something?",
                'Why dont you google that. |<a href="http://www.google.com" target="_blank">Google</a>'
                ]
    try:
        data = format_maths_string(string)
        _ops = data[1]
        nums = data[0]
        result = nums[0]
        maths = {'*': multiply, '+': add, '-': subtract, '/': divide, '^': power, '!': factoria}
        k = 1
        if len(nums) == 1:
            return string + ' = ' + str(maths['!'](data[0][0]))
        else:
            for i in _ops:
                result = maths[i](result, nums[k])
                k += 1

            return string + ' = ' + str(result)
    except Exception as e:
        return response[r.randrange(len(response))]
