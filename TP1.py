'''
11. Container With Most Water


You are given an integer array height of length n. 

There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 

In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
============
Input: height = [1,1]
Output: 1


Remember these three things:
- left and right are indexes.
- width = right - left.
- area = width X shorter height.


Why do we use min() instead of max()?
Water cannot be higher than the shorter wall. If one wall has height 3 and the other has height 7, the water height is only 3.


Operation	                                    Purpose

right - left	                                Calculate width
min(height[left], height[right])	            Find the water height
width * current_height	                        Calculate the area
max(max_area, area)	                            Keep the largest area found


Remember this simple rule for LeetCode 11:

The taller wall does not determine the water level. The shorter wall determines it, because water spills over the shorter side first.

'''




class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0 

        while left<right:
            width = right - left
            current_height = min(height[left],height[right])
            area = width * current_height

            max_area = max(max_area,area)

            if(height[left]<height[right]):
                left=left+1
            else:
                right = right-1
        return max_area


        






