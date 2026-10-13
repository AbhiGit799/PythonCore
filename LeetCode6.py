'''
334. Increasing Triplet Subsequence


Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: One of the valid triplet is (1, 4, 5), because nums[1] == 1 < nums[4] == 4 < nums[5] == 6.



One very important point

first and second are not necessarily the first and second elements of the array.

They mean:

first  = best/smallest candidate for position 1
second = best/smallest candidate for position 2


The key idea is: keep the smallest possible first, 
then the smallest possible second, and if anything is bigger than second, we win.


float('inf') means positive infinity.

So initially:

first  = ∞
second = ∞


'''

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = float('inf')
        second = float('inf')
        for num in nums:
            if num<=first:
                first = num
            elif num<=second:
                second = num
            else:
                return True
        return False


n = [1,2,3,4,5]

print(Solution().increasingTriplet(n));

'''
in first turn num = 1 first=inf, second=inf
so first = 1, second = inf 
now num = 2 first = 1, second = inf
so second = 2   
now num = 3 first = 1, second = 2
so return True
'''
















