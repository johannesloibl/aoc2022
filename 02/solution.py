from pathlib import Path
inp = Path("input.txt").read_text().splitlines(False)
games = [line.split() for line in inp]

score = dict(X=1, Y=2, Z=3)
winmap = {
    ("A", "X"): 3,
    ("A", "Y"): 6,
    ("A", "Z"): 0,
    ("B", "X"): 0,
    ("B", "Y"): 3,
    ("B", "Z"): 6,
    ("C", "X"): 6,
    ("C", "Y"): 0,
    ("C", "Z"): 3,
}
total = 0
for opp, you in games:
    total += score[you] + winmap[(opp, you)]
print(total)


# x loose 0
# y draw 3
# z win 6
# r 1
# p 2
# s 3
score = dict(X=0, Y=3, Z=6)
winmap = {
    ("A", "X"): 3,
    ("A", "Y"): 1,
    ("A", "Z"): 2,
    ("B", "X"): 1,
    ("B", "Y"): 2,
    ("B", "Z"): 3,
    ("C", "X"): 2,
    ("C", "Y"): 3,
    ("C", "Z"): 1,
}
total = 0
# games = [
#     ("A", "Y"), # 1+3
#     ("B", "X"), # 1+0
#     ("C", "Z"), # 1+6
# ]
for opp, you in games:
    # print(opp, you)
    # print(winmap[(opp, you)], score[you])
    total += score[you] + winmap[(opp, you)]
print(total)