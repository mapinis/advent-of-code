inp = open("Day 9.txt").readlines()[0]

score = 0
group = 0
garbage = False
numOfGarbage = 0
skip = False

for char in inp:
    if skip:
        skip = False
        continue
    if not garbage:
        if char == "{":
            group += 1
        elif char == "}":
            score += group
            group -= 1
        elif char == "<":
            garbage = True
    else:
        if char == "!":
            skip = True
        elif char == ">":
            garbage = False
        else:
            numOfGarbage += 1

print("Score:", score)
print("Chars Within Garbage:", numOfGarbage)