from pathlib import Path

contents = Path("input.txt").read_text().splitlines(False)


def char2score(c):
    if c.islower():
        return ord(c) - ord("a") + 1
    else:
        return ord(c) - ord("A") + 27


print(sum([char2score(c)
           for c in [set(line[:int(len(line) / 2)]).intersection(set(line[int(len(line) / 2):])).pop()
                     for line in contents]]))

sum = 0
while len(contents):
    s = set(contents.pop(0))
    s = s.intersection(contents.pop(0))
    s = s.intersection(contents.pop(0))
    sum += char2score(s.pop())
print(sum)


