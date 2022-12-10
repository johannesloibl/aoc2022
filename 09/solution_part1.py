from pathlib import Path
import time
from traits.api import HasTraits, Int, observe, Set, Instance, Event, Tuple, List
from pprint import pprint
t0 = time.perf_counter()
lines = Path("input.txt").read_text().splitlines(False)
# lines = Path("test.txt").read_text().splitlines(False)


directions = dict(
    #  x  y
    S=(0, 0),  # stay
    L=(-1, 0),
    R=(1, 0),
    U=(0, 1),
    D=(0, -1),
    RU=(1, 1),
    RD=(1, 1),
    LU=(-1, -1),
    LD=(-1, -1),
)

commands = []
for line in lines:
    parts = line.split(" ")
    commands.append((parts[0], int(parts[1])))


class Location(HasTraits):
    seen: set = Set(Tuple(Int, Int), value={(0, 0)})

    pos = List(Int, value=[0, 0])

    def move(self, direction: str, steps: int):
        print(direction, steps)
        dx, dy = directions[direction]
        for i in range(steps):
            self.move_delta(dx, dy)

    def move_to(self, x, y):
        print(f"{self.__class__.__name__} ({self.x}, {self.y}) -> ({x}, {y})")
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
    pass


class Tail(Location):

    head: Head = Instance(Head)

    @observe("head:pos")
    def on_head_moved(self, event):
        hx, hy = event.new[0], event.new[1]
        tx, ty = self.x, self.y
        dx = hx - tx
        dy = hy - ty

        if abs(dx) == 2 or abs(dy) == 2:
            self.move_to(event.old[0], event.old[1])


head = Head()
tail = Tail(head=head)


for direction, steps in commands:
    head.move(direction, steps)

pprint(tail.seen)
print(len(tail.seen))

