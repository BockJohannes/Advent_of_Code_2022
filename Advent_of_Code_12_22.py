from collections import deque
import numpy as np

grid = np.array([list(x) for x in open("test.txt").read().strip().splitlines()])
# start/end row/column (point)
for r, row in enumerate(grid):
    for c, item in enumerate(row):
        if item == "S":
            sr = r
            sc = c
            grid[r][c] = "a"
        if item == "E":
            er = r
            ec = c
            grid[r][c] = "z"
print(grid)

Part_1 = deque()
Part_1.append((0, sr, sc))

Part_2 = deque()
Part_2.append((0, er, ec))

def solve(p):
    if p == Part_1: visited = {(sr, sc)}
    else: visited = {(er, ec)}
    while p:
        steps, r, c = p.popleft()
        for new_row, new_column in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]: 
            print(new_row, new_column)
            if new_row < 0 or new_column < 0 or new_row >= len(grid) or new_column >= len(grid[0]):
                continue
            if (new_row, new_column) in visited:
                continue
            if p == Part_1:
                if ord(grid[new_row][new_column]) - ord(grid[r][c]) > 1:
                    continue
                if new_row == er and new_column == ec:
                    return steps + 1
                    exit(0)
            else:
                if ord(grid[new_row][new_column]) - ord(grid[r][c]) < -1:
                    continue
                if grid[new_row][new_column] == "a":
                    return steps + 1
                    #print(f"steps for S to E = {steps+1}")
                    exit(0)
        visited.add((new_row, new_column))
        if p == Part_1:
            Part_1.append((steps + 1, new_row, new_column))
        else:
            Part_2.append((steps + 1, new_row, new_column))

#print(solve(Part_1))
print(solve(Part_2))

