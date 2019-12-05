nums = [list(line.split("\t")) for line in open("Day 6.txt").readlines()]
nums = [list(int(num) for num in line) for line in nums][0]
history = [list(nums)]
steps = 0

while True:
    steps += 1
    m = max(nums)
    i = nums.index(m)
    nums[i] = 0
    for j in range(m):
        nums[(i + 1 + j) % len(nums)] += 1
    if nums in history:
        break
    history.append(list(nums))

print(steps - history.index(nums))