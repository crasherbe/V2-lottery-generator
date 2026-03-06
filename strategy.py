from collections import Counter

def analyze_history(history):

    digits = []

    for number in history:
        for d in number:
            digits.append(int(d))

    counter = Counter(digits)

    hot_numbers = [x[0] for x in counter.most_common(5)]
    cold_numbers = [x[0] for x in counter.most_common()[-3:]]

    return hot_numbers, cold_numbers
