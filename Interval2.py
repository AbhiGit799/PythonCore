'''
452. Minimum Number of Arrows to Burst Balloons

This is a Greedy Algorithm + Sorting + Interval problem.

Let's understand the question first, then the approach, and finally the Python code with a dry run.
1. Understand the question
You are given a 2D array called points.

Each balloon is represented by an interval:

[x_start, x_end]
- x_start: Where the balloon starts.
- x_end: Where the balloon ends.
You can shoot an arrow vertically from any X-coordinate.

If an arrow passes through a balloon's interval, that balloon bursts.

Your task: Find the minimum number of arrows required to burst all balloons.


2. What approach do we use?
We use Greedy + Sorting.

The main idea:
1. Sort balloons by their ending position.
2. Shoot the first arrow at the ending position of the first balloon.
3. Check whether the next balloon can be burst by the same arrow.
4. If yes, don't shoot another arrow.
5. If no, shoot another arrow at the ending position of that balloon.
Why sort by ending position?

Because shooting at the earliest ending point gives us the best chance of bursting as many overlapping balloons as possible.


'''


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        # Sort ballons by their ending position
        points.sort(key=lambda x:x[1])
        arrows = 1
        # Find arrow position for the first balloon
        arrow_position = points[0][1]
        for start,end in points:
            if start > arrow_position:
                arrows += 1
                arrow_position = end
        return arrows
    


obj = Solution()

totalarrow = obj.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])

print(totalarrow)




# s = [[10,16],[2,8],[1,6],[7,12]]

# s.sort(key=lambda x: x[1])

# print(s)



