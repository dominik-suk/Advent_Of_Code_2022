def readInputData(filename):
    result = []
    subArr = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            if line != "\n":
                subArr.append(int(line[:-1]))
            else:
                result.append(subArr)
                subArr = []
    return result

calories = readInputData("input.txt")
index = 0
max3 = 0
max1 = 0
for j in range(3):
    max = sum(calories[0])
    for i in range(len(calories)):
        if sum(calories[i]) > max:
            max = sum(calories[i])
            index = i
    if j == 0:
        max1 = max
    max3 += max
    calories.pop(index)

print(f"Answer part 1: {max1}\nAnswer part 2: {max3}")