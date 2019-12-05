inp = [int(num) for num in open("Day 5.txt").readlines()]
index = 0
newIndex = 0
steps = 0
while(True):
    try:
        if(inp[index] >= 3):
            inp[index] -= 1
            index += inp[index] + 1
        else: 
            inp[index] += 1
            index += inp[index] - 1
        steps += 1
    except:
        break

print(steps)