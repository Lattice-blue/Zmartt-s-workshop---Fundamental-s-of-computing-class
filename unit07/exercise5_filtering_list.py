#Medium, given a list of scores, create a second list containing only scores of 75 and above.

# I didn't even think of using tuples
scores_list = [
    ("Alice", 85),
    ("Bob", 42),
    ("Charlie", 98),
    ("Diana", 74),
    ("Ethan", 59),
    ("Fiona", 91),
    ("George", 12),
    ("Hannah", 67),
    ("Ian", 88),
    ("Julia", 100),
    ("Kevin", 53),
    ("Laura", 79),
    ("Michael", 31),
    ("Nina", 95),
    ("Oliver", 0),
    ("Paula", 63),
    ("Quinn", 82),
    ("Rachel", 70),
    ("Sam", 48),
    ("Tina", 93),
]

passed_scores = []

for score_pair in scores_list:
    if score_pair[1] >= 75:
        passed_scores.append(score_pair)

print(passed_scores)