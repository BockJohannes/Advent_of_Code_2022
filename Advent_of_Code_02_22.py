puzzle = open("02_22_input.txt").read()

#Rules
#A X 1 Rock
#B Y 2 Paper
#C Z 3 Scissors
#lose 0 | draw 3 | win 6

score = 0
score_2 = 0

for line in puzzle.split("\n"):
    if line == "A X":
        score += 4
        score_2 += 3
    if line == "A Y":
        score += 8
        score_2 += 4
    if line == "A Z":
        score += 3
        score_2 += 8
    if line == "B X":
        score += 1
        score_2 += 1
    if line == "B Y":
        score += 5
        score_2 += 5
    if line == "B Z":
        score += 9
        score_2 += 9
    if line == "C X":
        score += 7
        score_2 += 2
    if line == "C Y":
        score += 2
        score_2 += 6
    if line == "C Z":
        score += 6
        score_2 += 7

print(score)
print(score_2)
