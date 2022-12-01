import operator

class Elf:
    def __init__(self, calories):
        self.calories = calories        

    def add_calories(self, amount):
        self.calories += amount
    
    def get_calories(self):
        return self.calories

elfs = []
calories = 0
max = -1

f = open("input.txt", "r")
lines = f.readlines()

for line in lines:
        if line.strip():            
            calories += int(line.strip())
        else:
            elfs.append(Elf(calories))
            calories = 0

for elf in elfs:
    if elf.get_calories() > max:
        max = elf.get_calories()        

print("part 1: " + str(max))

sorted_elfs = sorted(elfs, key=operator.attrgetter('calories'))
sorted_elfs.reverse()
print("part 2: " + str(sorted_elfs[0].get_calories() + sorted_elfs[1].get_calories() + sorted_elfs[2].get_calories()))