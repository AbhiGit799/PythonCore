'''

LeetCode 27 – Remove Element
Easy
 Two Pointers
 In-place Array


Problem: LeetCode 27 – Remove Element
1. Understand the problem
You are given an array nums and a value val.

You need to:
1. Remove all occurrences of val from the array.
2. Modify the array in-place.
3. Return the number of elements that are not equal to val.

nums = [3, 2, 2, 3]
val = 3

Expected Result
nums = [2, 2, _, _]
return 2


Here _ means we don't care about the remaining elements.


2. Approach – Two Pointers
We use one pointer called k.
- i → checks every element in the array.
- k → tracks where the next valid element should be placed.
Logic:

If nums[i] != val:
- Copy nums[i] to nums[k].
- Increment k.
If nums[i] == val:

- Skip that element.


'''



class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k] = nums[i]
                k=k+1
        return k




    















