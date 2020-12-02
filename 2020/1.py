inp = open("2020/1.txt").readlines()
nums = list(map(int, inp))

# bad O(n^3) algorithm but only 200 inputs and I have orgo homework
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        s = nums[i] + nums[j]
        for k in range(j + 1, len(nums)):
            if s + nums[k] == 2020:
                print(nums[i] * nums[j] * nums[k])
                exit()