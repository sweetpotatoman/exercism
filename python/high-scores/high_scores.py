def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores[0:3]
    # return sorted(scores, reverse=True)[0:3]

# print(latest([10,20,30]))
# print(personal_best([10,20,30,20,100,50]))
# print(personal_top_three([10,20,30,200,140]))