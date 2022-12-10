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

def move_many_items(count, src, dst):
    print(f"move {count} from {src} to {dst}")
    crates = [stacks[src].pop() for _ in range(count)]
    stacks[dst].extend(crates[::-1])

for op in contents[10:]:
    op = op.replace("move ", "").replace("from ", "").replace("to ", "")
    move_many_items(*map(int, op.split(" ")))

pprint(stacks)

print("".join([stacks[col][-1] for col in range(1,10)]))





