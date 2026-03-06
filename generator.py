import random

def valid_pattern(num):

    even = sum(int(x) % 2 == 0 for x in num)
    odd = len(num) - even

    small = sum(int(x) <= 4 for x in num)
    big = len(num) - small

    if even >= 1 and odd >= 1 and small >= 1 and big >= 1:
        return True

    return False


def generate_numbers(digit, total, hot, cold):

    pool = hot + cold

    results = set()

    while len(results) < total:

        number = ""

        for _ in range(digit):
            number += str(random.choice(pool))

        if valid_pattern(number):
            results.add(number)

    return list(results)
