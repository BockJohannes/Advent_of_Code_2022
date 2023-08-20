puzzle = open("01_22_input.txt").read()

calories_max = 0
backpack = 0
elf_liste = []

for line in puzzle.split("\n"):
  if len(line) == 0:
    elf_liste.append(backpack)
    backpack = 0
  else:
    backpack += int(line)

  calories_max = max(calories_max, backpack)

print(f"Most Calories = {calories_max}")

elf_liste.sort()
print(f"Top 3 Elfs = {elf_liste[-3:]}")
print(f"Top 3 Gesamt = {sum(elf_liste[-3:])}")
