import re

puzzle = open("05_22_input.txt").read()
stack, move = puzzle.split("\n\n")
move_list = []
stack1 = [
        [],
        ['D','M','S','Z','R','F','W','N'],
        ['W','P','Q','G','S'],
        ['W','R','V','Q','F','N','J','C'],
        ['F','Z','P','C','G','D','L'],
        ['T','P','S'],
        ['H','D','F','W','R','L'],
        ['Z','N','D','C'],
        ['W','N','R','F','V','S','J','Q'],
        ['R','M','S','G','Z','W','V']
        ]

stack2 = [
        [],
        ['D','M','S','Z','R','F','W','N'],
        ['W','P','Q','G','S'],
        ['W','R','V','Q','F','N','J','C'],
        ['F','Z','P','C','G','D','L'],
        ['T','P','S'],
        ['H','D','F','W','R','L'],
        ['Z','N','D','C'],
        ['W','N','R','F','V','S','J','Q'],
        ['R','M','S','G','Z','W','V']
        ]

for line in move.split("\n"):
    move_list += [list(map(int,re.findall('\d+', line)))]

for moves in move_list:
    if len(moves) == 0: break
    # x=quantity | y=from | z=to
    x,y,z, = moves[0],moves[1],moves[2]
    counter = 1
    crane_list = []
    while counter <= x:
        crane = (stack1[y][-1])
        del (stack1[y][-1])
        stack1[z].append(crane)
        crane_list.append((stack2[y][-1]))
        del (stack2[y][-1])
        counter += 1
    crane_list.reverse()
    for item in crane_list:
        stack2[z].append(item)

Part1 = Part2 = ""
for i in range(1,len(stack1)):
    Part1 += stack1[i][-1]
    Part2 += stack2[i][-1]
