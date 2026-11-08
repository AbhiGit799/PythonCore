'''

Recursion – Solve the problem by calling the same function repeatedly.

Memoization – Recursion + storing previously calculated results.

Tabulation – Solve smaller problems first using a loop and an array.




What is Dynamic Programming (DP) in DSA?
Dynamic Programming (DP) is an algorithmic technique used to solve complex problems by breaking them into smaller subproblems, solving each subproblem only once, and storing its result so that we can reuse it later.

In simple words:

Dynamic Programming = Solve once + Store the result + Reuse it.


Two approaches to Dynamic Programming
=======================================
There are two main ways to implement DP.

Approach 1: Memoization (Top-Down)
Memoization means:
1. Start with recursion.
2. Store calculated results in a dictionary or array.
3. Before calculating, check whether the result is already available.
4. If available, reuse it


Approach 2: Tabulation (Bottom-Up)
Tabulation means solving smaller problems first and building up to the final answer.

Instead of recursion, we use loops.


4. Memoization vs Tabulation
Feature     	     Memoization	             Tabulation
Approach	         Top-Down	                 Bottom-Up
Uses	             Recursion	                 Loops
Storage	            Array/Dictionary	         Array
Calculates	        When needed	                 Usually all states
Recursion stack	     Yes	                       No






5. How to identify a Dynamic Programming problem?
Look for these clues:
- The problem asks for the maximum or minimum value.
- The problem asks for the number of possible ways.
- The problem involves choosing between different options.
- The same subproblems appear repeatedly.
- You need to optimize a result based on smaller decisions.
Examples:
- Minimum cost
- Maximum profit
- Number of ways to reach a destination
- Longest subsequence
- Minimum number of coins
Remember: These clues suggest DP, but not every maximum/minimum problem requires it.





'''


'''
1137. N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537


'''

'''

This problem is very similar to Fibonacci. The main difference is:

- Fibonacci uses the previous 2 numbers.
- Tribonacci uses the previous 3 numbers.

Let's understand it step by step using Python.

1. Understand the question
We are given an integer n.

We need to return the n-th Tribonacci number.

The Tribonacci sequence is defined as:

T(n) = T(n-1)+T(n-2)+T(n-3)

T(0) = 0
T(1) = 1
T(2) = 1

Tribonacci sequence
0, 1, 1, 2, 4, 7, 13, 24
First eight Tribonacci numbers

'''


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        return (self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3))


obj = Solution()
print(obj.tribonacci(4))  # Output: 4
