# A = Rock; B = Paper; C = Scissors
# X = Rock; Y = Paper; Z = Scissors
#      1          2           3
# loss = 0; Draw = 3; Win = 6
# 
# Rock > Scissors   Paper > Rock        Scissors > Paper
# Rock < Paper      Paper < Scissors    Scissors < Rock
#
# A > Z; B > X; C > Y
# A < Y; B < Z; C < X
#
# ---- part 2 ----
# X = Lose; Y = Draw; Z = Win
def read(filename):
    with open(filename) as f:
        result = []
        lines = f.readlines()
        for line in lines:
            result.append([line[0], line[2]])
    return result

def scoreWinDrawLoss(string1, string2):
    loss = 0; draw = 3; win = 6

    if   (string1 == "A" and string2 == "Z") or (string1 == "B" and string2 == "X") or (string1 == "C" and string2 == "Y"):
        return loss
    elif (string1 == "A" and string2 == "X") or (string1 == "B" and string2 == "Y") or (string1 == "C" and string2 == "Z"):
        return draw
    else:
        return win

def scoreRockPaperScissors(string):
    rock = 1; paper = 2; scissors = 3

    if string == "X":
        return rock
    if string == "Y":
        return paper
    if string == "Z":
        return scissors

def part2_ScoreWinDrawLoss(string):
    loss = 0; draw = 3; win = 6

    if string == "X":
        return loss
    if string == "Y":
        return draw
    if string == "Z":
        return win

def part2_ScoreRockPaperScissors(string1, string2):
    rock = 1; paper = 2; scissors = 3

    if   (string1 == "A" and string2 == "Y") or (string1 == "B" and string2 == "X") or (string1 == "C" and string2 == "Z"):
        return rock
    elif (string1 == "A" and string2 == "Z") or (string1 == "B" and string2 == "Y") or (string1 == "C" and string2 == "X"):
        return paper
    else:
        return scissors

guide = read("input.txt")
part1_Score = 0
part2_Score = 0
for round in guide:
    part1_Score += scoreWinDrawLoss(round[0], round[1]) + scoreRockPaperScissors(round[1])
    part2_Score += part2_ScoreWinDrawLoss(round[1]) + part2_ScoreRockPaperScissors(round[0], round[1])

print(f"Answer part 1: {part1_Score}\nAnswer part 2: {part2_Score}")