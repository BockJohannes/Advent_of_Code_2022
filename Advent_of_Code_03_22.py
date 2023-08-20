puzzle = open("03_22_input.txt").read()

rucksack = []
compartment = []

##### Part 1 #####
for line in puzzle.split("\n"):
    rucksack.append(line)
    Item1 = slice(0,len(line)//2)
    Item2 = slice(len(line)//2, len(line))
    for i in line[Item1]:
        if i in line[Item2]:
            compartment.append(i)
            break

##### Part 2 #####
x = 0
trup = []
while x <= 297:
    for i in rucksack[x]:
        if i in rucksack[x+1] and i in rucksack[x+2]:
            trup.append(i)
            break
    x +=3

def solve(x):
    summe = 0
    for char in x:
        summe += ord(char)-96 if char.islower() else ord(char)-38
    return summe

print(f"Summe Part 1 = {solve(compartment)}")
print(f"Summe Part 2 = {solve(trup)}")
