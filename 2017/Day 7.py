fil = open("Day 7.txt").readlines()

parents = []
children = []
useless = []

for line in fil:
    if ">" not in line:
        useless.append(line[:line.index(" ")])
        continue
    
    parents.append(line[:line.index(" ")])
    children += line[line.index(">") + 1:-1].replace(" ","").split(",")

print(set(parents) - (set(children) - set(useless)))