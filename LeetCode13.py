'''
1493. Longest Subarray of 1's After Deleting One Element

You are given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.


'''



class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        zeros = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            window_length = right - left + 1
            max_length = max(max_length, window_length - 1)

        return max_length


nums=[1,1,0,1]

obj = Solution()

print(obj.longestSubarray(nums))


'''

Yes! Exactly. 👍 You understood the main idea.
We include the zero in the window, but because we must delete one element, we subtract 1 from the window length when calculating the answer.


- right - left + 1 calculates the current window length.
- window_length - 1 accounts for deleting exactly one element.
- max() keeps the largest answer found so far.
One important detail: We don't physically remove the zero from the array. We only calculate what the length would be after deleting one element.


'''

'''

We'll go step by step, and then you can dry-run the code yourself.
1. Understand the problem
You are given an array containing only 0 and 1. You must delete exactly one element and return the length of the longest continuous sequence of 1s remaining.


One important difference from LeetCode 1004:
- LeetCode 1004: You can flip up to k zeros into ones.
- LeetCode 1493: You must delete exactly one element.


2. Approach: Variable-size sliding window
We can use the same two pointers:
- left — beginning of the window.
- right — end of the window.
- zeros — number of zeros inside the window.
Our rule: Keep at most one zero inside the window.
Why? Because we can delete that one zero to make the remaining elements all ones.
When the window contains more than one zero, move left forward until the window contains at most one zero.



'''




