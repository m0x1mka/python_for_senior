n = int(input())
nums = [i for i in range(1, n + 1)]
len_nums = {}
for i in nums:
    if sum([int(j) for j in str(i)]) not in len_nums.keys():
        len_nums[sum([int(j) for j in str(i)])] = [i]
    else:
        len_nums[sum([int(j) for j in str(i)])].append(i)
print(len(max(list(len_nums.values()), key=len)))
