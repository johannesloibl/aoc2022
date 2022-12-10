from pathlib import Path

stream = Path("input.txt").read_text()

distinct_chars = 4  # part 1
distinct_chars = 14  # part 2

for i in range(len(stream)):
    part = set(stream[i:i+distinct_chars])
    print(part)
    if len(part) == distinct_chars:
        print(i+distinct_chars)
        break






