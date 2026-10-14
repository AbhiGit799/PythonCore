'''

Lesson 1: What is Sliding Window?

Sliding Window is a technique used to solve problems involving continuous (contiguous) elements in an array or string.
Instead of repeatedly calculating the same values, we maintain a window of elements and slide it forward as we process the array.


Imagine you have an array of numbers and need to find the sum of every 3 consecutive elements.


1. Solve it without Sliding Window

nums = [2, 1, 5, 1, 3, 2]
k = 3

max_sum = 0

for i in range(len(nums) - k + 1):
    current_sum = 0

    for j in range(i, i + k):
        current_sum += nums[j]

    max_sum = max(max_sum, current_sum)

print(max_sum)

Output = 9

Here, we use two loops:
- The outer loop chooses where each window starts.
- The inner loop calculates the sum of the k elements in that window.

The problem is that we repeatedly add elements that we've already added before.

For example, the first window is [2, 1, 5], and the second is [1, 5, 1]. We calculate the sums of 1 and 5 again.

We can avoid this repeated work!





2. Solve it using Sliding Window

The key idea is:

New window sum = Previous window sum − outgoing element + incoming element


For example:
- Previous window: [2, 1, 5] → sum = 8
- Remove 2 → sum = 6
- Add 1 → sum = 7
- New window: [1, 5, 1] → sum = 7



Lesson 2: Two types of Sliding Window

There are two main patterns you should learn.

1. Fixed-size Sliding Window
The window size remains constant.
Example: Find the maximum sum of k consecutive elements.
Common problems: Maximum Average Subarray I, Maximum Sum Subarray of Size K.


2. Variable-size Sliding Window
The window grows or shrinks depending on a condition.
Example: Find the shortest subarray whose sum is at least a target, assuming positive numbers.
Common problems: Minimum Size Subarray Sum, Longest Substring Without Repeating Characters.


'''

# nums = [1, 4, 2, 10, 2, 3, 1]
# k = 3



def max_sum_subarray(nums,k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    print(f"Initial window sum: {window_sum}")
    # Slide the window from start to end in the array
    for i in range(k,len(nums)):
        window_sum = window_sum - nums[i-k] + nums[i]
        print(f"Window sum after sliding: {window_sum}")
        max_sum = max(max_sum, window_sum)

    return max_sum


print(max_sum_subarray([1, 4, 2, 10, 2, 3, 1],3)) 




'''

Since you've already learned fixed-size Sliding Window in LeetCode 643 and 1456, 
the main difference to understand is that a variable-size window can grow and shrink depending on a condition.

1. What is Variable-Size Sliding Window?
Imagine a window that covers some elements of an array.
- Expand the window: Move the right pointer forward to include more elements.
- Shrink the window: Move the left pointer forward to remove elements.
- Stop shrinking: When the window satisfies the required condition.





Yes, exactly! ✅ Variable-Size Sliding Window uses the Two Pointer technique.
They are closely related, but there is a small difference:
- Two Pointers is a general technique that uses two indexes to traverse or compare elements.
- Sliding Window is a specific pattern where two pointers define a continuous section of an array or string, and we expand or shrink that section.


2. Difference between common patterns

Technique	                     Example problem	              How pointers move
Two Pointers	                 Two Sum II	                      Move pointers based on the comparison
Fixed-Size Sliding Window	     LeetCode 1456	                  Move the window while maintaining size k
Variable-Size Sliding Window	 LeetCode 1004	                  Expand right; move left when the condition is violated


Our task is:
Find the longest contiguous subarray whose sum is at most 5.
Here, contiguous means the elements must be next to each other.


nums = [2, 1, 3, 2, 4]
target = 5

left = 0
window_sum = 0
max_length = 0

for right in range(len(nums)):   # Expand the window
    window_sum += nums[right]

    while window_sum > target:     # Shrink the window
        window_sum -= nums[left]
        left += 1

    max_length = max(max_length, right - left + 1)   # Update the answer

print(max_length)



'''



















