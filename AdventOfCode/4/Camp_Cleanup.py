def read(filename):
    with open(filename) as f:
        result = []
        lines = f.readlines()
        for line in lines:
            if line[-1] == "\n":
                result.append(line[:-1].split(","))
            else:
                result.append(line.split(","))
    return result

def does_contain(range1, range2):
    min1 = int(range1.split("-")[0]); max1 = int(range1.split("-")[1]); min2 = int(range2.split("-")[0]); max2 = int(range2.split("-")[1])
    if (
        ((min1<=min2<=max1) and (min1<=max2<=max1)) or
        ((min2<=min1<=max2) and (min2<=max1<=max2))
    ):
        return True
    else:
        return False

def does_overlap(range1, range2):
    min1 = int(range1.split("-")[0]); max1 = int(range1.split("-")[1]); min2 = int(range2.split("-")[0]); max2 = int(range2.split("-")[1])
    if (
        (min1<=max1<min2<=max2) or
        (min2<=max2<min1<=max1)
    ):
        return False
    else:
        return True

number_of_containments = 0
number_of_overlaps = 0
pairs = read("input.txt")
for pair in pairs:
    if does_contain(pair[0], pair[1]):
        number_of_containments += 1
    if does_overlap(pair[0], pair[1]):
        number_of_overlaps += 1

print(f"Answer part 1: {number_of_containments}\nAnswer part 2: {number_of_overlaps}")