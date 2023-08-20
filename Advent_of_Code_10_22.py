puzzle = []
clock = 0
x = 1
Part1 = []
picture = ''

with open("10_22_input.txt") as file:
    for line in file:
        if line[0] == 'n':
            com = line[:4]
            puzzle.append(com)
        else:
            value = line[4:]
            puzzle.append(int(value))

def signal(c, v):
    if c == 20 or c % 40 == 20:
        Part1.append(c*v)

def draw(c, v, pic):
    if (c % 40) in [v-1, v, v+1]:
        pic += '#' 
    else:
        pic += ' '
    if ((c+1) % 40) == 0:
        pic += '\n'
    return pic

for line in puzzle:
    if line == 'noop':
        clock += 1
        signal(clock, x)
        picture = draw(clock ,x, picture)
    else:
        clock += 1
        signal(clock, x)
        picture = draw(clock, x, picture)
        clock += 1
        signal(clock, x)
        x += line
        picture = draw(clock, x, picture) 

print(f"Part 1 = {sum(Part1)} \n")
print("Part 2")
print(picture)
