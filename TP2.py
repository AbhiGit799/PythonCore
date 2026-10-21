'''
1679. Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.


'''


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=0
        right = len(nums)-1
        count = 0
        while left<right:
            total = nums[left]+nums[right]

            if k==total:
                count = count+1
                left=left+1
                right=right-1
            
            elif total < k:
                left += 1
                
            else:
                right -= 1
            
        return count;


obj = Solution()

print(obj.maxOperations([1,2,3,4], k = 5))




'''
Approach = 2 pointer


Because the array is sorted:
- Moving left forward can only maintain or increase the sum.
- Moving right backward can only maintain or decrease the sum.
That's what makes the two-pointer approach work!


Remember this rule

Sum compared with k	Action on a sorted array

total < k	left += 1
total > k	right -= 1
total == k	Count the pair and move both

Important: Sorting is necessary for this particular two-pointer strategy, 
not for every possible solution. You can also solve this problem using a hash map without sorting.


Yes! ✅ You understood it correctly.

We sort the array so we can decide which pointer to move based on the sum.

Remember, sorting makes the values predictable when we move the pointers.

The key rules are:
- Sorted array + sum too small: Move left forward.
- Sorted array + sum too large: Move right backward.
- Sum equals k: Count the pair and move both pointers.

'''
        




















