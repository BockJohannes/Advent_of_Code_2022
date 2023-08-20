from dataclasses import dataclass
from typing import List


puzzle = open("07_22_input.txt")

@dataclass
class Dir:
    name: str
    dirs: List['Dir']
    size: int
    parent: 'Dir'

root = Dir('/', [],0,"")
current = root
for line in puzzle:
    data = line.split()
    if line == "$ cd /\n":
       continue
    elif data[0] == '$':
        if data[1] == "ls":
            continue
        elif data[1] == "cd":
            if not data[2] == "..":
                for i in range(len(current.dirs)):
                    if current.dirs[i].name == data[2]:
                        current = current.dirs[i]
                        break
            else: 
                current.parent.size += current.size
                current = current.parent
    elif data[0] == "dir":
        current.dirs.append(Dir(data[1],[],0,current))
    else:
        current.size += int(data[0])
while not current.name == '/':
    current.parent.size += current.size
    current = current.parent

def part1(currentdir, result1):
    if currentdir.size <= 100000:
        result1 += currentdir.size
    for directories in currentdir.dirs:
        result1 = part1(directories, result1)
    return result1

free = 70000000 - root.size
reqspace = 30000000 - free

def part2(currentdir, result, required):
    res = result
    if currentdir.size >= required and currentdir.size < result:
        res = currentdir.size
    for directory in currentdir.dirs:
        res = part2(directory, res, required)
    return res

print("Part1: ",part1(root, 0), "Part2: ", part2(root, 999999999, reqspace))
