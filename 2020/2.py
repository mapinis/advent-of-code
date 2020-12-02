import collections as col

# How many passcodes are valid?


inp = open("2020/2.txt").readlines()

def part1(inp):
    # [min]-[max] [char]: [password]
    Datum = col.namedtuple("Datum", ["char", "min", "max", "password"])

    data = []
    # process input
    for line in inp:
        a = line.split(" ")
        a[0] = a[0].split("-")
        data.append(Datum(a[1][0], int(a[0][0]), int(a[0][1]), a[2].strip()))


    # count valid passwords
    count = 0
    for d in data:
        if d.min <= d.password.count(d.char) <= d.max:
            count += 1

    print(count)

def part2(inp):
    # [pos1]-[pos2] [char]: [password]
    # at most one of these
    Datum = col.namedtuple("Datum", ["char", "pos1", "pos2", "password"])

    data = []
    # process input
    for line in inp:
        a = line.split(" ")
        a[0] = a[0].split("-")
        data.append(Datum(a[1][0], int(a[0][0]), int(a[0][1]), a[2].strip()))


    # count valid passwords
    count = 0
    for d in data:
        a = int(d.password[d.pos1 - 1] == d.char) + int(d.password[d.pos2 - 1] == d.char)
        if a == 1:
            count += 1

    print(count)

part2(inp)