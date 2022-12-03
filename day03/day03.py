f = open("input.txt", "r")
lines = f.readlines()

result1 = 0
result2 = 0

for line in lines:
    goto1 = False
    goto2 = False
    for c1 in range(0, int(len(line.strip())/2)):        
        if goto1 is False:
            for c2 in range(int(len(line.strip())/2), len(line.strip())):                       
                if line[c1].__eq__(line[c2]):
                    if line[c1].isupper():
                        result1 += ord(line[c1])-38      # 65 - A
                    elif line[c1].islower():
                         result1 += ord(line[c1])-96     # 97 - a
                    goto1 = True
                    goto2 = True
                    break
        else:
            break
    if goto2 is True:
        continue            

print("Part 1: " + str(result1))

for x, line in enumerate(lines):
    goto3 = False
    goto4 = False
    if x % 3 == 0:            
        if goto4 is False:
            for c1 in lines[x+0]:               
                    for c2 in lines[x+1]:                        
                        if goto3 is False:
                            if c1.__eq__(c2):
                                for c3 in lines[x+2]:
                                    if c1.__eq__(c3):
                                        if c1.isupper():
                                            result2 += ord(c1)-38      # 65 - A
                                        elif c1.islower():
                                            result2 += ord(c1)-96     # 97 - a
                                        goto3 = True
                                        goto4 = True
                                        break
                        else:
                            break
        else:
            break
                                               
print("Part 2: " + str(result2))