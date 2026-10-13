'''
238. Product of Array Except Self


Given an integer array nums, return an array answer such that answer[i] is equal to the product 
of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30


'''



class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product = product * nums[j]
            result.append(product)
        return result

        
obj = Solution()
arr = [1, 2, 3, 4]

print(obj.productExceptSelf(arr));


'''

For each index, we exclude the current number and multiply everything on its left and right.

Time: O(n)
Extra space: O(1) excluding the required output array.

So for every element:

answer = product of elements on LEFT × product of elements on RIGHT

Python's range() can be:
=========================
range(start, stop, step)



Easy way to remember
=======================
range(n)

➡️ moves left to right

0 → 1 → 2 → 3

while

range(n - 1, -1, -1)

➡️ moves right to left

3 → 2 → 1 → 0

The second one is extremely common in DSA when you need to process an array backwards.

'''

class Solution:

    def productExceptSelf(self, nums: list[int]) -> list[int]:

        n = len(nums)
        result = [1] * n

        # Calculate prefix products
        prefix = 1

        for i in range(n):
            result[i] = prefix
            prefix = prefix * nums[i]

        # Calculate suffix products
        suffix = 1

        for i in range(n - 1, -1, -1):
            result[i] = result[i] * suffix
            suffix = suffix * nums[i]

        return result
