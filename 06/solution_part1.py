from pathlib import Path
from typing import *
import bisect

lines = Path("input.txt").read_text().splitlines(False)

dir_sizes = dict()


class Directory:
    def __init__(self, name: str, parent: Optional["Directory"]):
        self.name = name
        self.parent = parent
        self.files = list()
        self.subdirs: Dict[str, "Directory"] = dict()

    def calc_size(self):
        global dirs_with_size_lt_100000, dir_sizes
        total = sum(self.files) + sum([d.calc_size() for d in self.subdirs.values()])
        dir_sizes[self.name] = total
        return total


tree = Directory("/", None)

workdir: Optional[Directory] = tree


def ls(cmd: str):
    print(cmd)


def file(cmd: str):
    print(cmd)
    global workdir
    workdir.files.append(int(cmd.split(" ")[0]))


def dir(cmd: str):
    print(cmd)
    global workdir
    cmd = cmd.replace("dir ", "")
    workdir.subdirs[cmd] = Directory(cmd, workdir)


def cd(cmd: str):
    print(cmd)
    global workdir, tree
    cmd = cmd.replace("$ cd ", "")
    if cmd == "/":
        workdir = tree
    elif cmd == "..":
        workdir = workdir.parent
    else:
        workdir = workdir.subdirs[cmd]


for cmd in lines[1:]:
    if cmd.startswith("$ cd"):
        cd(cmd)
    elif cmd.startswith("$ ls"):
        ls(cmd)
    elif cmd.startswith("dir"):
        dir(cmd)
    else:
        file(cmd)

tree.calc_size()
sorted_dir_sizes = sorted(dir_sizes.values())

dirs_with_size_lt_100000 = 0
for size in sorted_dir_sizes:
    if size > 100000:
        break
    dirs_with_size_lt_100000 += size
print("Answer part 1:", dirs_with_size_lt_100000)

free = 70000000 - dir_sizes["/"]
to_free = 30000000 - free
print("Answer part 2:", sorted_dir_sizes[bisect.bisect(sorted_dir_sizes, to_free)])
