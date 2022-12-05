def readStacks(filename):
    with open(filename) as f:
        arr = []
        lines = f.readlines()
        for line in lines:
            subArr = []
            if line == "\n":
                break
            for char in range(len(line)):
                if (char - 1) % 4 == 0:
                    subArr.append(line[char])
            arr.append(subArr)
        arr.pop()

        result = []
        for i in range(9):
            result.append([])

        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] != " ":
                    result[j].append(arr[i][j])

        for i in range(9):
            result[i] = result[i][::-1]

    return result

def readMoves(filename):
    with open(filename) as f:
        arr = []
        lines = f.readlines()
        moves_found = False
        for line in lines:
            if moves_found and line[-1] == "\n":
                arr.append(line[:-1].split())
            if moves_found and line[-1] != "\n":
                arr.append(line.split())
            if line == "\n":
                moves_found = True
        result = []
        for i in range(len(arr)):
            subArr = []
            for j in arr[i]:
                try:
                    subArr.append(int(j))
                except:
                    pass
            result.append(subArr)
    return result

def move_crate(stacks, move, part):
    for i in range(move[0]):
        if part == 1:
            save = stacks[move[1] - 1][-1]
            stacks[move[1] - 1].pop()
            stacks[move[2] - 1].append(save)
        elif part == 2:
            save = stacks[move[1] - 1][i - move[0]]
            stacks[move[2] - 1].append(save)
    if part == 2:
        for i in range(move[0]):
            stacks[move[1] - 1].pop()

part1_stacks = readStacks("input.txt")
part2_stacks = readStacks("input.txt")
moves = readMoves("input.txt")

for move in moves:
    move_crate(part1_stacks, move, 1)
    move_crate(part2_stacks, move, 2)

top_crates = ""
part2_top_crates = ""
for stack in range(len(part1_stacks)):
    top_crates += str(part1_stacks[stack][-1])
    part2_top_crates += str(part2_stacks[stack][-1])

print(f"Answer part 1: {top_crates}\nAnswer part 2: {part2_top_crates}")