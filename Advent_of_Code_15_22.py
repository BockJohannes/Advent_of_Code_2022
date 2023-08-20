import re
#from collections import defaultdict
import z3

puzzle = []

def read_puzzle_input(file, puzzle):
    with open(file) as f:
        for line in f:
            puzzle.append(list(map(int, re.findall('\-?\d+', line))))
    return puzzle            

def solve(puzzle, from_x, to_x, y_value):
    counter = 0
    for x in range (from_x,to_x):
        if x % 100_000 == 0:
            print(x)
        y = y_value
        pos = True
        # sensor x/y and beacon x/y
        for sx,sy,bx,by in puzzle:
            if (x,y) == (bx,by):
                pos = True
                break
            if dist(sx,sy,x,y) <= dist(sx,sy,bx,by):
                pos = False
                break
        if not pos:
            counter += 1
    return counter

dist = lambda x1,y1,x2,y2 : abs(y2-y1) + abs(x2-x1)

### Test ###
#read_puzzle_input("test.txt", puzzle)
#print("Test : ", solve(puzzle, -400, 400, 10))

### Part 1 ###
read_puzzle_input("15_22_input.txt", puzzle)
print("Part 1: ",solve(puzzle,-9_000_000, 9_000_000, 2_000_000))

### Part 2 ###
s = z3.Solver()
x, y = z3.Int("x"), z3.Int("y")

s.add(0 <= x); s.add(x <= 4_000_000)
s.add(0 <= y); s.add(y <= 4_000_000)

def z3_abs(x):
    return z3.If(x >= 0, x, -x)

for sx, sy, bx, by in puzzle:
    m = dist(sx,sy,bx,by)
    s.add(z3_abs(sx - x) + z3_abs(sy - y) > m)
    
assert s.check() == z3.sat
model = s.model()
print("Part 2: ", model, model[x].as_long() * 4_000_000 + model[y].as_long())
