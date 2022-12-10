from pathlib import Path
import numpy as np
import time
from pprint import pprint
t0 = time.perf_counter()
lines = Path("input.txt").read_text().splitlines(False)

forest = np.array([
    list(map(int, line)) for line in lines
])

def search_array(array: np.array, invert: bool) -> set:
    treemap = set()

    forest = array.transpose() if invert else array

    for nrow, row in enumerate(forest):
        rowlen = len(row)
        # left to right
        highest_tree_seen_lr = -1
        for ncol, tree in enumerate(row):
            if tree > highest_tree_seen_lr:
                highest_tree_seen_lr = tree
                index = (nrow, ncol)
                treemap.add(index if not invert else index[::-1])

        highest_tree_seen_rl = -1
        for ncol, tree in enumerate(row[::-1]):
            if tree > highest_tree_seen_rl:
                highest_tree_seen_rl = tree
                index = (nrow, rowlen - ncol - 1)
                treemap.add(index if not invert else index[::-1])
            if highest_tree_seen_lr == highest_tree_seen_rl:
                break

    return treemap


treemap = search_array(forest, invert=False)
treemap.update(search_array(forest, invert=True))

print(len(treemap))
print(time.perf_counter() - t0)






