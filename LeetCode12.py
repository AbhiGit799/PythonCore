'''
1. Understand the problem

You are given:
- nums: an array containing only 0s and 1s.
- k: the maximum number of zeros you are allowed to flip into ones.
Return the maximum number of consecutive ones you can obtain after flipping at most k zeros.

Example:
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2


We can flip at most two zeros into ones.

For example, we could flip two zeros in this window:

[1, 1, 1, 0, 0]

After flipping:
[1, 1, 1, 1, 1]

That gives us five consecutive ones. But can we find a longer window? Yes!

The goal is to find the longest window containing at most k zeros.

The important rule is:
We can have at most k zeros inside the window. Since k = 2, the window can contain two zeros, but not three.



Valid Window Example
*********************
Window: [1, 1, 1, 0, 0]
Number of zeros = 2. Still valid!
Window length = 5, so our current maximum is 5.


Invalid Window Example
***********************
Window: [1, 1, 1, 0, 0, 0]
Number of zeros = 3. Invalid! We are allowed only 2 zeros.


What do we do when the window becomes invalid?
**********************************************
This is the most important part.
When the number of zeros becomes greater than k, we move left forward until the window becomes valid again.

1. Remember the rule
In LeetCode 1004, we can flip at most k = 2 zeros into ones.
That means our window can contain:
- 0 zeros → valid
- 1 zero → valid
- 2 zeros → valid
- 3 zeros → invalid
When the window has 3 zeros, we need to remove elements from its beginning until only 2 or fewer zeros remain.


'''




class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zeros = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros = zeros + 1
            while zeros > k:
                if nums[left]==0:
                    zeros = zeros-1
                left = left+1
            max_length = max(max_length,right-left+1)
        
        return max_length

nums = [1,1,1,0,0,0,1,1,1,1,0]; k = 2

obj = Solution()

print(obj.longestOnes(nums,k))

        
'''
Code	                               Meaning
left = 0	                           Start of the window
zeros = 0	                           Count zeros in the window
max_length = 0	                       Longest valid window found so far
for right in range(len(nums))	       Expand the window one element at a time
if nums[right] == 0	                   If the new element is zero, count it
while zeros > k	                       If there are too many zeros, shrink the window
if nums[left] == 0	                   If the element being removed is zero, decrease the zero count
left += 1	                           Move the beginning of the window forward
right - left + 1	                   Calculate the window length
return max_length	                   Return the longest valid length


Remember these three things:
1. right expands the window.
2. left shrinks the window when there are too many zeros.
3. max_length remembers the longest valid window found.



'''









