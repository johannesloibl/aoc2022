from pathlib import Path
inp = Path("input.txt").read_text()

elfs_sum = sorted([sum(map(int, section.split("\n")))
                   for section in inp.split("\n\n")], reverse=True)
print(elfs_sum[0])  # Part 1
print(sum(elfs_sum[:3]))  # Part 2

