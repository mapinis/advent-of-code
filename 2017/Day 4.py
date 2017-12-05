inp = list(map(lambda line: line.strip("\n").split(" "), open("Day 4.txt").readlines()))
corr = 0
for line in inp:
    for phrase in line:
        if line.count(phrase) != 1:
            break
    else:
        corr += 1

print(corr)
