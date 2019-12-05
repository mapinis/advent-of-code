inp = open("Day 4.txt").readlines()
inp = [list(line.strip("\n").split(" ")) for line in inp]
inp = [list(list(sorted(list(phrase)) for phrase in line)) for line in inp]
corr = 0
for line in inp:
    for phrase in line:
        if line.count(phrase) != 1:
            break
    else:
        corr += 1

print(corr)