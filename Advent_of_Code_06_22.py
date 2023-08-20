puzzle = open("06_22_input.txt").read()

def solve_puzzle(x):
    char = 0 
    while char <= (len(puzzle)-x):
        packet = []
        for i in range(x):
            if puzzle[char+i] not in packet:
                packet.append(puzzle[char+i])
            else: break
        if len(packet) == x:
            solution = ''.join(packet)
            marker = char + x
            return solution, marker
        else: char += 1

print(solve_puzzle(4))
print(solve_puzzle(14))
