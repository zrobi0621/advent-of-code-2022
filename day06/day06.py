f = open("input.txt", "r")
line = f.readline()

for x, c in enumerate(line):    
        arr = []
        count = 0

        if x != len(line) - 3:            
            for i in range(0, 4):            
                arr.append(line[x+i]) 
        else:
            break

        for i in arr:
            for j in range(0,4):                
                if i.__ne__(arr[j]):                    
                    count += 1

        if count == 12:            
            break
        
print("Part 1 : " + str(x + 1 + 4))

for y, c in enumerate(line):    
        arr2 = []
        count2 = 0
        
        if y != len(line) - 13:            
            for i in range(0, 14):            
                arr2.append(line[y+i]) 
        else:
            break
        
        for i in arr2:
            for j in range(0, 14):                
                if i.__ne__(arr2[j]):                    
                    count2 += 1
        
        if count2 == 182:            
            break

print("Part 2 : " + str(y + 14))                                                           