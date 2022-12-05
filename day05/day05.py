f = open("input.txt", "r")
lines = f.readlines()

column = int(len(lines[0]) / 4)
stack = [ [] for _ in range(column) ]
s = 0

for index, line in enumerate(lines):        
    if line[1].__eq__("1"):        
        break
    else:
        s += 1                                          # stack
        for x, i in enumerate(line):
            if ((x + 1) % 4 == 0) and (x != 0):                        
                if line[x - 2].__ne__(" "):                                    
                    stack[int((x + 1) / 4) - 1].append(line[x - 2])

for i in range(index + 2, len(lines)):                  # moves
    print(lines[i])                                                                                  
    quantity = int(lines[i].split(" ")[1])
    fr = int(lines[i].split(" ")[3])
    to = int(lines[i].split(" ")[5])

    #for i in range(0, quantity):                       # part 1
    #    stack[to - 1].insert(0, stack[fr - 1][0])
    #    stack[fr - 1].remove(stack[to - 1][0])                

    tmp = []
    for i in range(0, quantity):                        # part 2
        tmp.append(stack[fr - 1][0])
        stack[fr - 1].remove(stack[fr - 1][0])

    tmp.reverse()
    
    for i in range(0,quantity):
        stack[to - 1].insert(0, tmp[i])
    
result = ""
for i in stack:
    result += i[0]
    
print("part 1/2: " + str(result))