def latest(scores):
    return scores.pop()


def personal_best(scores):
    scores.sort(reverse=True)
    return scores[0]


def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores[0:3] if len(scores) >= 3 else scores[0: len(scores)]
