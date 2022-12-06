def read(file):
    with open(file) as f:
        string = f.readlines()[0]
    return string

def isUnique(chars):
    for j in range(len(chars)):
        for k in range(len(chars)):
            if j < k and chars[j] == chars[k]:
                return False
    return True

def getMarker(signal):
    part1_result = []; part2_result = []
    for i in range(len(signal)):
        part1_chars = []; part2_chars = []
        for j in range(14):
            if i + j < len(signal) - 3 and j <= 4:
                part1_chars.append(signal[i+j])
            if i + j < len(signal) - 13:
                part2_chars.append(signal[i+j])
        if isUnique(part1_chars):
            part1_result.append(i + 4)
        if isUnique(part2_chars):
            part2_result.append(i + 14)
    return part1_result[0], part2_result[0]

marker = getMarker(read("input.txt"))
print(f"Answer part 1: {marker[0]}\nAnswer part 2: {marker[1]}")