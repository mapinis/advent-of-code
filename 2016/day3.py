data = open("day3.txt")
triangles = data.readlines()
possible = 0

for triangle in triangles:
    for x in range(len(triangle)):
        if(triangle[x] != " "):
            triangle = triangle[x:]
            break
    triangle = triangle.split()
    for x in range(len(triangle)):
        triangle[x] = int(triangle[x])
    triangle = sorted(triangle)
    print(triangle)
    if(int(triangle[0]) + int(triangle[1]) > int(triangle[2])):
        possible += 1

print(possible)