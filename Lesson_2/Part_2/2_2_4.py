nums = list(map(int, input().split()))
lst = []
for i in set(nums):
    if nums.count(i) > 1 and i not in lst:
        lst.append(i)
print(*sorted(lst))
