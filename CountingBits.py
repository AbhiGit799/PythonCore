'''
338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.

Do not solve it with built-in functions (i.e., like __builtin_popcount in C++).
 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10


Number	Binary	Number of 1s
0	      0	       0
1	      1	       1
2	     10	       1
3	     11	       2
4	    100	       1
5	    101	       2


'''

class Solution:
    def countBits(self, n: int) -> list[int]:

        dp = [0] * (n + 1)

        for i in range(1, n + 1):

            dp[i] = dp[i >> 1] + (i & 1)

        return dp


obj = Solution()

n=5

print(obj.countBits(n))


'''

What is dp?
dp = [0] * (n + 1)

dp is simply a list (array) where we store the answers.

Since n = 5, we need answers for numbers 0, 1, 2, 3, 4, 5.

That's 6 numbers.

Therefore:

dp = [0, 0, 0, 0, 0, 0]

Think of dp like a notebook:
Index	Meaning
dp[0]	Number of 1s in binary of 0
dp[1]	Number of 1s in binary of 1
dp[2]	Number of 1s in binary of 2
dp[3]	Number of 1s in binary of 3
dp[4]	Number of 1s in binary of 4
dp[5]	Number of 1s in binary of 5

We will fill this notebook with answers.

for i in range(1, 6):

So i takes these values:

1, 2, 3, 4, 5

Why are we starting from 1 instead of 0?

Because we already know the answer for 0:

dp[0] = 0

Now we need to calculate the answers for 1 to 5.

4. The most important line

dp[i] = dp[i >> 1] + (i & 1)

Let's understand this using a simple example.

The idea is:

Count of 1s in the current number = Count of 1s in the number after removing its last binary digit + the last binary digit itself.

For example, consider number 5.

5 = 101

Remove the last digit:

10 = 2


We already know that binary 10 contains one 1.

The removed digit was also 1.

Therefore:

Count of 1s in 5 = Count of 1s in 2 + 1
                 = 1 + 1
                 = 2


This is the logic behind our formula.

Now let's understand the two Python operators.             


A. What does i >> 1 mean?

This is called the right shift operator.

It removes the last binary digit.

Example:
5 >> 1

Binary representation:

5 = 101

Right shift by 1:

    10

Answer = 2


B. What does i & 1 mean?
This is called the bitwise AND operator.

For our problem, we use it to check the last binary digit.

Example:
5 & 1

Binary representation:

  101   (5)
& 001   (1)
-----
  001   (1)

Result = 1.

Another example:

4 & 1


  100   (4)
& 001   (1)
-----
  000   (0)


Result = 0.

So remember:
- If the last binary digit is 1, i & 1 returns 1.
- If the last binary digit is 0, i & 1 returns 0.





'''






