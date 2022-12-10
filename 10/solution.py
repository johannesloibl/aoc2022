from pathlib import Path
import numpy as np

lines = Path("input.txt").read_text().splitlines(False)
# lines = Path("test.txt").read_text().splitlines(False)


def splitval(cmd: str):
    return int(cmd.split(" ")[-1])


adds = np.zeros(240)
cycle = 0
for i, cmd in enumerate(lines):
    if cmd == "noop":
        cycle += 1
    if cmd.startswith("addx"):
        cycle += 2
        adds[cycle] = splitval(cmd)

x = 1 + np.cumsum(adds).astype(np.int64)
strength = (x * np.arange(1, 241)).astype(np.int64)
print("Part 1: ", sum((strength[np.arange(19, 220, 40)])))

pixels = np.zeros(240).astype(np.int64)
for i in range(240):
    xi = x[i]
    if i % 40 in (xi, xi - 1, xi + 1):
        pixels[i] = 1

for row in pixels.reshape((6, 40)):
    print("".join([(".", "#")[i] for i in row]))

print("Part 2: ZUPRFECL")

