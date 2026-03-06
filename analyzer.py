from collections import Counter

def strongest_digits(numbers):

    digits = []

    for num in numbers:
        for d in num:
            digits.append(d)

    counter = Counter(digits)

    return counter.most_common(10)
