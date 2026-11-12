'''
Monotonic Stack from absolute basics. 

1. What is a Stack?
A stack is a data structure that follows:

LIFO = Last In, First Out

- You put a new plate on top.
- You remove a plate from the top.
- You cannot directly remove a plate from the middle.

In Python, we use a list as a stack.

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)
# [10, 20, 30]


To remove the top element:

stack.pop()

print(stack)
# [10, 20]

The last inserted element (30) was removed first.


2. What is a Monotonic Stack?
Now let's understand the word Monotonic.

Monotonic means following a consistent order.

For example:

Increasing order:

[10, 20, 30, 40, 50]

Every next number is greater than the previous number.

Decreasing order:

[50, 40, 30, 20, 10]

Every next number is smaller than the previous number.

A Monotonic Stack is simply a stack where we maintain elements in increasing or decreasing order.

There are two common types.

3. Type 1: Monotonic Increasing Stack

Let's insert these numbers:

numbers = [10, 20, 30, 15]

We want the stack to remain in increasing order.

Step 1: Insert 10
stack = [10]


Step 2: Insert 20

20 is greater than 10.

stack = [10, 20]


Step 3: Insert 30

30 is greater than 20.

stack = [10, 20, 30]

Step 4: Insert 15

Here is the interesting part!

Current stack:

[10, 20, 30]

We want to insert 15.

But 15 is smaller than 30.

So remove 30 using pop().

[10, 20]


Now 15 is still smaller than 20.

Remove 20.

[10]

Now 15 is greater than 10.

Insert 15.

[10, 15]

Increasing order maintained

The final stack is:


[10, 15]


4. Type 2: Monotonic Decreasing Stack
Now let's do the opposite.

We want the stack to remain in decreasing order.

Input:
numbers = [50, 40, 30, 45]



Step 1: Insert 50
stack = [50]



Step 2: Insert 40

40 is smaller than 50.
stack = [50, 40]



Step 3: Insert 30

30 is smaller than 40.
stack = [50, 40, 30]



Step 4: Insert 45

45 is greater than 30.

Remove 30.
[50, 40]



45 is also greater than 40.

Remove 40.
[50]



45 is smaller than 50.

Insert 45.
[50, 45]



Decreasing order maintained

5. Compare both types
Feature	             Increasing Stack	           Decreasing Stack
Order	             Small → Large	               Large → Small
Example	             [10,20,30]	                   [30,20,10]
When to pop	         New value is smaller	       New value is greater

Note: These describe the values from bottom to top of the stack.

6. Python code for both types

Monotonic Increasing Stack
**************************
numbers = [10, 20, 30, 15]

stack = []

for num in numbers:

    while stack and stack[-1] > num:
        stack.pop()

    stack.append(num)

print(stack)

O/P => [10, 15]


Monotonic Decreasing Stack
**************************
numbers = [50, 40, 30, 45]

stack = []

for num in numbers:

    while stack and stack[-1] < num:
        stack.pop()

    stack.append(num)

print(stack)

O/P => [50, 45]


7. Where do we use Monotonic Stack in LeetCode?
It is especially useful for finding:
- Next Greater Element
- Next Smaller Element
- Previous Greater Element
- Previous Smaller Element

Some important LeetCode problems:

Problem	                                    Difficulty
496. Next Greater Element I	                Easy
739. Daily Temperatures	                    Medium
901. Online Stock Span	                    Medium
503. Next Greater Element II	            Medium
84. Largest Rectangle in Histogram	        Hard


Q1. What does monotonic increasing mean?
10, 20, 30, 40


Q2. In a monotonic decreasing stack, when do we pop?
When the new number is greater than the top

Q3. We have stack = [10, 20, 30]. New number = 15. What is the final increasing stack?
[10, 15]


Remember this simple rule:
***************************
while stack and stack[-1] < num: means:

"While the stack is not empty AND its top element is smaller than the new number, keep removing the top element."


'''



stack = [50, 40, 30]

print(stack[-1])

'''

LeetCode 739 – Daily Temperatures

This problem is a classic Monotonic Stack problem.

Let's understand it step by step using Python, with a simple example and a dry run.
1. Understand the question
You are given an array of daily temperatures.

For each day, you need to find how many days you must wait until a warmer temperature occurs.

If there is no warmer temperature in the future, return 0.

Example:
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

Expected output:
[1, 1, 4, 2, 1, 1, 0, 0]

Important: We need the number of days to wait, not the warmer temperature itself.

2. Approach: Monotonic Stack
We will use:
1. A result array initialized with zeros.
2. A stack to store the indexes of days.
3. A loop to visit each temperature.
Why store indexes instead of temperatures?

Because we need to calculate the number of days between two days:


2. Which approach do we use?
We use Monotonic Decreasing Stack.

Before understanding that term, remember:
- Stack follows LIFO (Last In, First Out).
- We store day indexes in the stack, not temperatures.
- We use indexes to calculate the number of days between two temperatures.
Our strategy:
1. Traverse the temperature array from left to right.
2. Store the current day's index in the stack.
3. If today's temperature is greater than the temperature at the index on top of the stack:
   - Pop the previous day.
   - Calculate the waiting days.
   - Store the answer in the result array.
4. Repeat until the stack is empty or the condition is false.

'''

print("\n")

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)

        stack = []

        for current_day, current_temp in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < current_temp:

                previous_day = stack.pop()

                result[previous_day] = current_day - previous_day

            stack.append(current_day)

        return result


temperatures = [73,74,75,71,69,72,76,73]

obj = Solution()
print(obj.dailyTemperatures(temperatures))



