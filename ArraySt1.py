'''
LeetCode 88 – Merge Sorted Array
Easy
 Two Pointers
 In-place Array


Problem: LeetCode 88 – Merge Sorted Array

We need to merge two sorted arrays into one sorted array.

The important point is that we must modify nums1 directly without creating another array.


nums1 = [1, 2, 3, 0, 0, 0]
m = 3

nums2 = [2, 5, 6]
n = 3

m = 3 means the first 3 elements of nums1 are valid.
n = 3 means all 3 elements of nums2 are valid.

The remaining zeros in nums1 are empty spaces.

Output
======
[1, 2, 2, 3, 5, 6]


Approach – Three Pointers
We use three pointers:
Pointer	Position	Purpose
i	m - 1	Last valid element in nums1
j	n - 1	Last element in nums2
k	m + n - 1	Last position in nums1

Why start from the end?

Because nums1 already has empty spaces at the end. We can place the largest elements there without overwriting the existing valid elements.






'''


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n-1

        while j>=0:
            if i>=0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i = i-1
            else:
                nums1[k] = nums2[j]
                j=j-1

            k = k-1

nums1 = [1,2,3,0,0,0]

print(nums1)

m = 3; nums2 = [2,5,6];n = 3

obj = Solution()

obj.merge(nums1,m,nums2,n)

print(nums1)


















