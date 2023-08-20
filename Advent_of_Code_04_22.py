puzzle = open("04_22_input.txt").read()

sum1 = sum2 = 0

for line in puzzle.split("\n"):
    if len(line) == 0: break
    pair1, pair2 = line.split(',')
    v1, v2 = pair1.split('-')
    v3, v4 = pair2.split('-')
    if int(v1)<=int(v3) and int(v2)>=int(v4) or int(v3)<=int(v1) and int(v4)>=int(v2):
        sum1 += 1

    list1 = []
    list2 = []
    x = int(v1)
    y = int(v3)
    while x <= int(v2):
        list1.append(x)
        x += 1
    while y <= int(v4):
        list2.append(y)
        y +=1
    for num in list1:
        if num in list2: 
            sum2 += 1
            break

print(f"part 1 = {sum1}")
print(f"part 2 = {sum2}")
