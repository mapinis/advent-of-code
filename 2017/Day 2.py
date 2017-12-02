print(sum(list(map(lambda line: max(line) - min(line), list(map(lambda line: list(map(lambda num: int(num), line.split("\t"))), open("Day 2.txt").readlines()))))))

# No, I did not write it this way, I just wanted to see if I could do this in 1 python line