nums = [2,4,1,3,5]

prefix = [0] * len(nums)

print(prefix)

prefix = [0] * len(nums)

prefix[0] = nums[0]

print(prefix)

for i in range(1,len(nums)):
    prefix[i] = prefix[i-1]+nums[i]

print(prefix)


'''
Line 1:
prefix = [0] * len(nums)
Creates a list of five zeros:
[0, 0, 0, 0, 0]


Line 2:
prefix[0] = nums[0]
The first prefix sum is simply the first number, which is 2.




'''












