import numpy as np
from pathlib import Path
import time
from traits.api import HasTraits, Int, observe, Set, Instance, Str, Tuple, List
from pprint import pprint

t0 = time.perf_counter()
lines = Path("input.txt").read_text().splitlines(False)
# lines = Path("test.txt").read_text().splitlines(False)
# lines = Path("test2.txt").read_text().splitlines(False)

directions = dict(
    #  x  y
    L=(-1, 0),
    R=(1, 0),
    U=(0, 1),
    D=(0, -1),
)

commands = []
for line in lines:
    parts = line.split(" ")
    commands.append((parts[0], int(parts[1])))


class Location(HasTraits):
    name: str = Str()
    seen: set = Set(Tuple(Int, Int), value={(0, 0)})

    pos = List(Int, value=[0, 0])

    def __repr__(self):
        return f"{self.name}: {tuple(self.pos)})"

    def move_to(self, x, y):
        print(f"{self.name} ({self.x}, {self.y}) -> ({x}, {y})")
        self.seen.add((self.x, self.y))
        self.pos = [x, y]
        self.seen.add((x, y))

    def move_delta(self, dx, dy):
        self.move_to(self.x + dx, self.y + dy)

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]


class Head(Location):
    name = "H"


class Knot(Location):
    parent_knot: Location = Instance(Location)

    @observe("parent_knot:pos")
    def on_parent_knot_moved(self, event):
        hx, hy = event.new[0], event.new[1]
        tx, ty = self.x, self.y
        dx = hx - tx
        dy = hy - ty
        adx = abs(dx)
        ady = abs(dy)

        if (adx, ady) in ((2, 2), (2, 1), (1, 2)):
            self.move_delta(dx // adx, dy // ady)
        elif adx == 2:
            self.move_delta(dx // adx, 0)
        elif ady == 2:
            self.move_delta(0, dy // ady)


head = Head()
knot1 = Knot(name="1", parent_knot=head)
knot2 = Knot(name="2", parent_knot=knot1)
knot3 = Knot(name="3", parent_knot=knot2)
knot4 = Knot(name="4", parent_knot=knot3)
knot5 = Knot(name="5", parent_knot=knot4)
knot6 = Knot(name="6", parent_knot=knot5)
knot7 = Knot(name="7", parent_knot=knot6)
knot8 = Knot(name="8", parent_knot=knot7)
knot9 = Knot(name="9", parent_knot=knot8)

for direction, steps in commands:
    print("---- ", direction, steps, " ----")
    dx, dy = directions[direction]
    for i in range(steps):
        head.move_delta(dx, dy)
    # input()

# pprint(knot9.seen)
print(len(knot9.seen))
