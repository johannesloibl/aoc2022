from pathlib import Path
from collections import defaultdict
from pprint import pprint

contents = Path("input.txt").read_text().splitlines(False)

stacks = defaultdict(list)
for row in range(8):
    for i, col in enumerate(range(9)):
        crate = contents[row][(col * 4) + 1]
        if crate != " ":
            stacks[i+1].insert(0, crate)

def move_items(count, src, dst):
    print(f"move {count} from {src} to {dst}")
    for i in range(count):
        crate = stacks[src].pop()
        stacks[dst].append(crate)

for op in contents[10:]:
    op = op.replace("move ", "").replace("from ", "").replace("to ", "")
    move_items(*map(int, op.split(" ")))

pprint(stacks)

print("".join([stacks[col][-1] for col in range(1,10)]))





