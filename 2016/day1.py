start = [0, 0]
# x, y
end = [0, 0]
directions = ["N", "E", "S", "W"]
direction = 0
i = "L4, R2, R4, L5, L3, L1, R4, R5, R1, R3, L3, L2, L2, R5, R1, L1, L2, R2, R2, L5, R5, R5, L2, R1, R2, L2, L4, L1, R5, R2, R1, R1, L2, L3, R2, L5, L186, L5, L3, R3, L5, R4, R2, L5, R1, R4, L1, L3, R3, R1, L1, R4, R2, L1, L4, R5, L1, R50, L4, R3, R78, R4, R2, L4, R3, L4, R4, L1, R5, L4, R1, L2, R3, L2, R5, R5, L4, L1, L2, R185, L5, R2, R1, L3, R4, L5, R2, R4, L3, R4, L2, L5, R1, R2, L2, L1, L2, R2, L2, R1, L5, L3, L4, L3, L4, L2, L5, L5, R2, L3, L4, R4, R4, R5, L4, L2, R4, L5, R3, R1, L1, R3, L2, R2, R1, R5, L4, R5, L3, R2, R3, R1, R4, L4, R1, R3, L5, L1, L3, R2, R1, R4, L4, R3, L3, R3, R2, L3, L3, R4, L2, R4, L3, L4, R5, R1, L1, R5, R3, R1, R3, R4, L1, R4, R3, R1, L5, L5, L4, R4, R3, L2, R1, R5, L3, R4, R5, L4, L5, R2"
i = i.replace(",", "")
i = i.split(" ")

print(i)

def go(dir, amount):
    global end
    if(directions[dir] == "N"):
        end[1] += amount
    elif(directions[dir] == "S"):
        end[1] -= amount
    elif(directions[dir] == "E"):
        end[0] += amount
    elif(directions[dir] == "W"):
        end[0] -= amount

for direct in i:
    if(direct[0] == "R"):
        direction += 1
    else:
        direction -= 1
    direction = direction % 4
    go(direction, int(direct[1:]))

print(end)
print(abs(start[0] - end[0]) + abs(start[1] - end[1]))