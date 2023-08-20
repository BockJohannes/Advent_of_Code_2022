import functools
part1, group, part2 = [], [], []

with open("AdventOfCode13.txt") as file:
    for line in file:
        line = line.strip()
        if line == '':
            part1.append(group)
            group = []
        else:
            group.append(eval(line))
        if line != '':
            part2.append(eval(line))

def solve(left, right):
    if type(left) is list and type(right) is list:
        for a, b in zip(left, right):
            res = solve(a, b)
            if res != 0:
                return res
            continue
        return len(left) - len(right)
    elif type(left) is list and type(right) is int:
        return solve(left, [right])
    elif type(left) is int and type(right) is list: 
        return solve([left], right)
    elif type(left) is int and type(right) is int:
        return left - right

sum_index = 0
for index, (a, b) in enumerate(part1):
    if solve(a, b) < 0:
        #print(index)
        sum_index += index + 1

part2.append([[2]])
part2.append([[6]])
part2.sort(key=functools.cmp_to_key(solve))

print("Part 1: ", sum_index)
print("Part 2: ", (1+part2.index([[2]]))*(1+part2.index([[6]])) )
