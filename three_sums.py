nums = [2,7,11,15,3,6]
target = 20
res = []

for i in range(len(nums)):
    seen = {}
    for j in range(i + 1, len(nums)):
        need = target - nums[i] - nums[j]
        if need in seen:
            res.append([i, seen[need], j])
        seen[nums[j]] = j

print(res)
