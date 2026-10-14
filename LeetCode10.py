'''

643. Maximum Average Subarray I


You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value 
and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000


'''

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        # Slide the window from start to end in the array
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, window_sum)
    
        return max_sum/k;

obj = Solution()
print(obj.findMaxAverage([1,12,-5,-6,50,3],4))


print(obj.findMaxAverage([5, 5, 5, 5, 5],3))


'''


1. Understand the problem
You are given an integer array nums and an integer k.
Find a contiguous subarray of exactly k elements that has the maximum average, and return that average.

The formula for average is:

Average = Sum of elements / k


2. Python solution using Sliding Window


3. Understand the important lines

Line 1: Calculate the first window
window_sum = sum(nums[:k])

Line 2: Slide the window
for i in range(k, len(nums)):

Why do we start at index 4? Because indexes 0 through 3 are already included in the first window.


Line 3: The sliding window formula
window_sum = window_sum - nums[i - k] + nums[i]

This is the most important line to understand.
During the first iteration, i = 4:

window_sum = window_sum - nums[0] + nums[4]

4. Why do we find the maximum sum instead of the maximum average?
Every window contains exactly k elements. Since we divide every window sum by the same positive number k, the window with the largest sum must also have the largest average.
So, we only need to track the maximum sum and divide once at the end.



5. Complexity analysis
Complexity	Explanation
Time: \(O(n)\)	Each element is processed at most once during the sliding step.
Space: \(O(1)\) auxiliary	We use only a few variables, not an additional array.
The initial sum(nums[:k]) takes \(O(k)\) time, so total time is \(O(k+n-k)=O(n)\).


'''











