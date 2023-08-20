puzzle = []

with open("09_22_input.txt") as file:
    for line in file:
        move, value = line.strip().split()
        puzzle.append([move, int(value)])

visited = set()
visited.add((0, 0))

start = [[0, 0], [0, 0]]

dp = dict()
dp['U'] = [0, 1]     #up
dp['D'] = [0, -1]    #down
dp['L'] = [-1, 0]    #left
dp['R'] = [1, 0]     #right

for move in puzzle:
    direction = move[0]
    steps = move[1]

    for _ in range(steps):
       start[1][0] += dp[direction][0]
       start[1][1] += dp[direction][1]
       if abs(start[1][0] - start[0][0]) < 2 and abs(start[1][1] - start[0][1]) < 2:
           continue

       if abs(start[1][0] - start[0][0]) != 0:
           if start[0][0] < start[1][0]:
               start[0][0] += 1
           else:
               start[0][0] -= 1

       if abs(start[1][1] - start[0][1]) != 0:
           if start[0][1] < start[1][1]:
               start[0][1] += 1
           else:
               start[0][1] -= 1
       visited.add((start[0][0], start[0][1]))

print(len(visited))

