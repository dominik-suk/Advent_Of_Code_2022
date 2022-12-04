def part1_read(filename):
    with open(filename) as f:
        result = []
        lines = f.readlines()
        for line in lines:
            result.append([line[:int(len(line)/2)], line[int(len(line)/2):-1]])
    return result

def part2_read(filename):
    with open(filename) as f:
        result = []
        lines = f.readlines()
        for group in range(len(lines)):
            if group % 3 == 0:
                result.append([lines[group][:-1], lines[group + 1][:-1], lines[group + 2][:-1]])
    return result

def get_priority_score(item):
    ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(ascii_letters)):
        if ascii_letters[i] == item:
            return i + 1

part1_priority_score = 0
rucksacks = part1_read("input.txt")
for rucksack in rucksacks:
    found = False
    for item1 in rucksack[0]:
        for item2 in rucksack[1]:
            if item1 == item2:
                part1_priority_score += get_priority_score(item1)
                found = True
                break
        if found:
            break

part2_priority_score = 0
rucksacks = part2_read("input.txt")
for group in rucksacks:
    found = False
    for item1 in group[0]:
        for item2 in group[1]:
            for item3 in group[2]:
                if item1 == item2 and item2 == item3:
                    part2_priority_score += get_priority_score(item1)
                    found = True
                    break
            if found:
                break
        if found:
            break

print(f"Answer part 1: {part1_priority_score}\nAnswer part 2: {part2_priority_score}")