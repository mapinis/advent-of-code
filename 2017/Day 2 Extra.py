inp = list(map(lambda line: sorted(list(map(lambda num: int(num), line.split("\t")))), open("Day 2.txt").readlines()))

results = []
for line in inp:
    for num in line:
        for num2 in line:
            if num % num2 == 0 and num / num2 > 1:
                results.append(num / num2)

print(sum(results))