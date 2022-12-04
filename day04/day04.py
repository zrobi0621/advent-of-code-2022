f = open("input.txt", "r")
lines = f.readlines()

s = False
arr1 = []
arr2 = []
tokenTemp = []
count = 0
count2 = 0

for line in lines:    
    contains = 0
    for token in line.strip().split(","):
        if s is False:        
            tokenTemp = token
            arr1 = list(range(int(token.split("-")[0]) ,int(token.split("-")[1]) + 1))
            s = True
        else:
            arr2 = list(range(int(token.split("-")[0]) ,int(token.split("-")[1]) + 1))
            s = False
            
            for i in arr1:
                if i in arr2:
                    contains += 1     

    if contains.__eq__((int(token.split("-")[1]) - int(token.split("-")[0])) + 1) or contains.__eq__((int(tokenTemp.split("-")[1]) - int(tokenTemp.split("-")[0])) + 1):
        count += 1  # Part1
    if contains >= 1:           
        count2 += 1 # Part2

print("Part 1: " + str(count))        
print("Part 2: " + str(count2))                