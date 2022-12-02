f = open("input.txt", "r")
lines = f.readlines()

result1 = 0
result2 = 0

for line in lines:
    
    # AX - Rock, BY - Paper, CZ - Scissors
    if line.strip()[0].__eq__("A"):
        if line.strip()[2].__eq__("X"):
            result1 += 3 + 1
        elif line.strip()[2].__eq__("Y"):
            result1 += 6 + 2
        elif line.strip()[2].__eq__("Z"):
            result1 += 0 + 3
    elif line.strip()[0].__eq__("B"):
        if line.strip()[2].__eq__("X"):
            result1 += 0 + 1
        elif line.strip()[2].__eq__("Y"):
            result1 += 3 + 2
        elif line.strip()[2].__eq__("Z"):
            result1 += 6 + 3
    elif line.strip()[0].__eq__("C"):
        if line.strip()[2].__eq__("X"):
            result1 += 6 + 1
        elif line.strip()[2].__eq__("Y"):
            result1 += 0 + 2
        elif line.strip()[2].__eq__("Z"):
            result1 += 3 + 3
            
print("Part 1: " + str(result1))

for line in lines:
    
    # A - Rock, B - Paper, C - Scissors | X - Lose, Y - Draw, Z - Win
    if line.strip()[0].__eq__("A"):
        if line.strip()[2].__eq__("X"):
            result2 += 3 + 0
        elif line.strip()[2].__eq__("Y"):
            result2 += 1 + 3
        elif line.strip()[2].__eq__("Z"):
            result2 += 2 + 6
    elif line.strip()[0].__eq__("B"):
        if line.strip()[2].__eq__("X"):
            result2 += 1 + 0
        elif line.strip()[2].__eq__("Y"):
            result2 += 2 + 3
        elif line.strip()[2].__eq__("Z"):
            result2 += 3 + 6
    elif line.strip()[0].__eq__("C"):
        if line.strip()[2].__eq__("X"):
            result2 += 2 + 0
        elif line.strip()[2].__eq__("Y"):
            result2 += 3 + 3
        elif line.strip()[2].__eq__("Z"):
            result2 += 1 + 6
            
print("Part 2: " + str(result2))
