f = "14_22_input.txt"
#f = "test.txt"

file = open(f)
puzzle = [[[int(coord) for coord in path.split(",")]for path in line.split("->")]for line in file.read().strip().split("\n")]

grid = set()
print(puzzle)
def compare_lists(list1, list2, grid):
    x1, y1 = list1
    x2, y2 = list2
    grid.add((x1,y1))
    grid.add((x2,y2))
    if x1 == x2:
        if y1 < y2:
            while y1 < y2:
                grid.add((x1,y1))
                y1 += 1
        else:
            while y1 > y2:
                grid.add((x1,y1))
                y1 -= 1
    else:
        if x1 < x2:
            while x1 < x2:
                grid.add((x1,y1))
                x1 += 1
        else:
            while x1 > x2:
                grid.add((x1,y1))
                x1 -= 1

def build_cave(stones):
    l = 0
    for _ in stones:
        for x in range(len(stones[l])):
            if stones[l][x] == stones[l][-1]:   
                break
            else:
                compare_lists(stones[l][x], stones[l][x+1], grid)
        l += 1

def sand_sim():
    sand_counter = 0
    x,y = 500, 0
    sand_falling = [x,y]

    while True:
        if y >= deepest_point:
            return sand_counter
        if (x,y+1) not in grid:
            y += 1
            sand_falling = x,y
        else:
            if (x-1,y+1) not in grid:
                x -= 1
                y += 1
                sand_falling = x,y
            else:
                if (x+1,y+1) not in grid:
                    x += 1
                    y += 1
                    sand_falling = x,y
                else:
                    if (x,y) not in grid:
                        grid.add((x,y))
                        x,y = 500, 0
                        sand_counter += 1 

build_cave(puzzle)
deepest_point = max(pos[1] for pos in grid)
print("Part 1: ",sand_sim())
