import numpy as np

with open("08_22_input.txt") as puzzle:
    lines = puzzle.read().strip().split()

grid = np.array([list(map(int, list(line))) for line in lines])

xAxis = yAxis = len(grid)
visible = scenic_score = 0

for x in range(xAxis):
    for y in range(yAxis):
        pos = grid[x, y]

        if y == 0 or np.amax(grid[x, :y]) < pos:
            visible += 1
        elif y == yAxis - 1 or np.amax(grid[x, (y+1):]) < pos:
            visible += 1
        elif x == 0 or np.amax(grid[:x, y]) < pos:
            visible += 1
        elif x == xAxis - 1 or np.amax(grid[(x+1):, y]) < pos:
            visible += 1

print(visible)

def scenic_score(x, y):
    view = 1
    for j in range(y-1, -1, -1):
        if grid[j][x] >= grid[y][x]: break
    view *= y - j
    for j in range(y+1, len(grid)):
        if grid[j][x] >= grid[y][x]: break
    view *= j - y
    for i in range(x-1, -1, -1):
        if grid[y][i] >= grid[y][x]: break
    view *= x - i
    for i in range(x+1, len(grid)):
        if grid[y][i] >= grid[y][x]: break
    view *= i - x
    return view

best_view = 0
for x in range(1, len(grid)-1):
    for y in range(1, len(grid)-1):
        best_view = max(best_view, scenic_score(x,y))

print(best_view)

