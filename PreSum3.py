'''
724. Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:
==========
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11


Example 2:
==========
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.


Example 3:
===========
Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0

'''

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            left_sum = left_sum + nums[i]

        return -1


obj= Solution()

print(obj.pivotIndex([2,1,-1]))

print(obj.pivotIndex([1,7,3,6,5,6]))



'''

5. Complexity
- Time: O(n) — one pass to calculate the total and another to check indices.
- Extra space: O(1) — we use only a few variables, not an additional prefix sum array.

'''

# ===========================================================================================================================================================

# Dry Run

'''

Let's do a step-by-step dry run for nums = [2, 1, -1] using our 
Find Pivot Index (LeetCode 724) solution.


total = 2+1+(-1)=2

Initial Values:

total = 2
left_sum = 0

right_sum = total - left_sum - nums[0]
          = 2 - 0 - 2
          = 0


Since left_sum == right_sum, the condition is true.

return 0

Important: 
===========
The loop stops at index 0. It does not check indices 1 or 2, because we've already found the leftmost pivot.



5. Final takeaway
Even though the current element is 2, it is excluded from both sums.
- Left sum = 0 (no elements on the left).
- Right sum = 1 + (-1) = 0.
- Both sums are equal.
Output: 0

Notice that we don't need to build a separate prefix sum array. 
The variable left_sum acts as a running sum, 
and total lets us calculate the right sum using subtraction.




'''
# ===========================================================================================================================================================

# Important Note

'''

Great question! The formula isn't something you need to memorize blindly. 
Let's derive it using basic maths so you can figure it out yourself in other DSA problems.

1. Start with what we know

Suppose: nums = [2, 1, -1]


Imagine the current element is `2` at index `0`.

The array has three parts:

## Left
# 0

## Current
# 2

## Right
# 1, -1

The entire array is made up of these three parts.

Therefore:

Total = Left Sum  + Current Element + Right Sum

This is the starting point. We're just adding up every element in the array, without missing or double-counting any.

===========================================================================================================================================================

2. Rearrange the equation

We want to find `Right Sum`.

Start with =====> Total = Left Sum + Current Element + Right Sum 

Subtract `Left Sum` from both sides:

Total-Left Sum = Current Element + Right Sum 


Now subtract `Current Element` from both sides:

Total- Left Sum - Current Element = Right Sum 

So we get:

Right Sum = Total - Left Sum - Current Element

That's it! We derived the formula using ordinary subtraction.

===========================================================================================================================================================

3. Verify it with our example

nums = [2, 1, -1]
total = 2
left_sum = 0
current_element = 2

Substitute these values:

Right Sum = 2-0-2 = 0

The actual right-side elements are:

1+(-1)=0 

Both results match!

===========================================================================================================================================================

4. How to think like a DSA programmer

Whenever you see a problem like this, ask yourself three questions:

1. What do I know? The total sum of the array.
2. What do I need? The sum on the right side.
3. What can I subtract? The left sum and the current element, because neither belongs to the right side.

This is a useful problem-solving habit: start with a relationship you know, then rearrange it to calculate what you need.

Remember: Don't just memorize the formula. 
Understand that the total contains the left side, current element, and right side. Removing the first two leaves the right side.

===========================================================================================================================================================


'''




