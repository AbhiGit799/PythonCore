'''

LeetCode 215 – Kth Largest Element in an Array

This problem is based on Heap (Priority Queue), Sorting, and Quickselect.

For beginners, let's first understand the question, then learn the easiest solution, and finally explore the optimal Heap approach.

1. Understand the question

You are given an array of numbers and an integer k.

Find the kth largest element in the array.

Important: We need the kth largest element, not the kth distinct largest element.

Example 1

nums = [3, 2, 1, 5, 6, 4]
k = 2

Let's sort the array in descending order:

[6, 5, 4, 3, 2, 1]


Position	       Number
1st largest	        6
2nd largest	        5
3rd largest	        4
4th largest	        3
5th largest	        2
6th largest	        1

Since k = 2, our answer is:
5



What is a Heap?
*****************
A Heap is a special tree-based data structure that helps us efficiently access the smallest or largest element.

Python provides a built-in module:

import heapq

Python's heapq implements a Min Heap.

What is a Min Heap?
In a Min Heap, the smallest element is always at the top.

For example:

nums = [3, 2, 1, 5, 6, 4]

After creating a Min Heap, the smallest element is accessible at index 0.

We can use this property to solve our problem.
Main idea
We only need the K largest elements.

Instead of sorting all elements, we maintain a Min Heap containing only K elements.

Rules:
1. Add elements to the heap.
2. If heap size becomes greater than K, remove the smallest element.
3. After processing all elements, the heap contains the K largest elements.
4. The smallest element among those K elements is our answer.
Why?

Because the smallest of the K largest elements is exactly the Kth largest element.

but 


'''


import heapq
from typing import List

def findKthLargest(nums: List[int], k: int) -> int:
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap,num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]

nums = [3,2,1,5,6,4]; k = 2

print(findKthLargest(nums,k))



'''

Approach 1: Sorting (Beginner-friendly)
The easiest approach is to sort the array in descending order.

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]


'''




