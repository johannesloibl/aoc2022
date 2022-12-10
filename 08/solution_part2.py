from pathlib import Path
import numpy as np
import time
from pprint import pprint
t0 = time.perf_counter()
lines = Path("input.txt").read_text().splitlines(False)
# lines = Path("test.txt").read_text().splitlines(False)

forest = np.array([
    list(map(int, line)) for line in lines
])

scenic_score = np.zeros(forest.shape)

nrows, ncols = forest.shape

def is_edge(row, col):
    return row in (0, nrows - 1) or col in (0, ncols - 1)

def is_invalid_index(row, col):
    return row in (-1, nrows) or col in (-1, ncols)


for (row, col), tree in np.ndenumerate(forest):
    if is_edge(row, col):
        continue  # Edges always have a score of 0
    score = 1
    #                 left     right   up       down
    for direction in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        trees_in_sight = 0
        new_row = row
        new_col = col
        while True:
            new_row += direction[0]
            new_col += direction[1]
            if is_invalid_index(new_row, new_col):
                break

            checked_tree = forest[new_row, new_col]
            trees_in_sight += 1
            if checked_tree >= tree:
                break
        score *= trees_in_sight
    scenic_score[row, col] = score

pprint(scenic_score)
print("Max score:", max(scenic_score.flatten()))


print(time.perf_counter() - t0)






