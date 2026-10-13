# 1431. Kids With the Greatest Number of Candies

# There are n kids with candies. You are given an integer array candies, 
# where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, 
# denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, 
# after giving the ith kid all the extraCandies, they will have the 
# greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.

 

# Example 1:

# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 


'''

We use a two-step approach: first find the maximum candies, then check each kid against that maximum.

Approach: Find Maximum + Traverse


Given:

candies = [2, 3, 5, 1, 3]
extraCandies = 3
Step 1: Find the maximum
max = 5

This tells us the current greatest number of candies.

Step 2: Check every kid

For each kid:

candies[i] + extraCandies >= max

If this is true → true
Otherwise → false

Example:

Kid 1: 2 + 3 = 5  >= 5 → true
Kid 2: 3 + 3 = 6  >= 5 → true
Kid 3: 5 + 3 = 8  >= 5 → true
Kid 4: 1 + 3 = 4  >= 5 → false
Kid 5: 3 + 3 = 6  >= 5 → true

Result:

[true, true, true, false, true]

Why this approach?

We don't actually need to give candies to anyone. We are only asking:

"If I give all extra candies to this kid, can they reach or exceed the current maximum?"

So we just calculate:

newCandies = candies[i] + extraCandies

and compare it with max.


'''


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int):
        maxcandie = max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies >= maxcandie:
                candies[i] = True
            else:
                candies[i] = False
        return candies
        


obj = Solution()
print(obj.kidsWithCandies([2,3,5,1,3], 3)) 


'''

For every kid, pretend you give that kid all the extra candies and check whether their new total is at least as large as the current maximum.

This is a simple array traversal + maximum value problem, and it can be solved in O(n) time.


1. What is the problem asking?

Suppose we have:

candies = [2, 3, 5, 1, 3]
extraCandies = 3

There are 5 kids.

| Kid   | Current candies |
| ----- | --------------: |
| Kid 1 |               2 |
| Kid 2 |               3 |
| Kid 3 |               5 |
| Kid 4 |               1 |
| Kid 5 |               3 |


You have 3 extra candies.

The question asks:

For each kid, if we give all 3 extra candies to that kid, will that kid have the greatest number of candies?


2. First find the current greatest number
candies = [2, 3, 5, 1, 3]

The maximum is:

5

So 5 is the target.

3. Check each kid
Kid 1

Kid 1 has:

2

Give them 3 extra:

2 + 3 = 5

They can reach the greatest number (5).

So:

true
Kid 2
3 + 3 = 6

6 is greater than 5.

So:

true
Kid 3
5 + 3 = 8

8 is greater than 5.

So:

true
Kid 4
1 + 3 = 4

4 is less than 5.

So:

false
Kid 5
3 + 3 = 6

6 is greater than 5.

So:

true

Therefore:

[true, true, true, false, true]
4. The important logic

The easiest way to think about the problem is:

Find the maximum candies any kid currently has.

For every kid:
    Add extraCandies to their candies.
    Check if the result >= maximum.

    If yes → true
    If no  → false

Notice that we use:

>=

not:

>

because multiple kids can have the greatest number of candies.

For example:

candies = [2, 3, 5]
extraCandies = 2

Maximum = 5

For Kid 1:

2 + 2 = 4 → false

For Kid 2:

3 + 2 = 5 → true

For Kid 3:

5 + 2 = 7 → true

Result:

[false, true, true]

Both Kid 2 and Kid 3 can have the greatest number.


'''









