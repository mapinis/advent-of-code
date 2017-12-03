inp = int(input("Num: "))
spiralNum = 1
spiralRange = list(range(2, 10))
while(inp not in spiralRange):
    spiralRange = list(range(spiralRange[-1] + 1, (spiralRange[-1] + 1) + (spiralNum + 1) * 8))
    spiralNum += 1

# Now I know the spiral num, it is the number of spirals after 1
# This num is the maximum amount of steps that it takes to get to center of this spiral

# Now to find the amount of steps to 1 from center:
fromCenter = spiralNum

# Now to find the specific number of steps to center for number (hardest)
spiralRange.insert(0, spiralRange.pop())
rowLength = spiralNum * 2 + 1
rows = []
for i in range(int(len(spiralRange) / (spiralNum + 1))):
    spiralRange.insert(rowLength * (i + 1), spiralRange[(rowLength - 1 + rowLength * i) % len(spiralRange)])
for i in range(spiralNum - 1):
    spiralRange.pop()
for i in range(int(len(spiralRange) / rowLength)):
    rows.append(spiralRange[rowLength * (i): rowLength * (i + 1)])

centerIndex = rowLength - spiralNum - 1
toCenter = 0
for row in rows:
    if inp in row:
        index = row.index(inp)
        toCenter = abs(centerIndex - index)

print(fromCenter + toCenter)
