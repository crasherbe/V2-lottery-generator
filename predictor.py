from collections import Counter

def top_predictions(numbers):

    digit_list = []

    for num in numbers:
        for d in num:
            digit_list.append(d)

    counter = Counter(digit_list)

    strongest_digits = [x[0] for x in counter.most_common(5)]

    scored = []

    for num in numbers:

        score = 0

        for d in num:
            if d in strongest_digits:
                score += 1

        scored.append((num, score))

    scored.sort(key=lambda x: x[1], reverse=True)

    top10 = [x[0] for x in scored[:10]]

    return top10
