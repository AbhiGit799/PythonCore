'''
LeetCode 901 – Online Stock Span
Let's solve this problem step by step using Stack (Monotonic Stack) in Python.

Medium
 Monotonic Stack

1. Understand the question
You are given stock prices one day at a time.

For each day, you need to calculate the stock span.

Stock span means:
The number of consecutive days, including today, for which the stock price was less than or equal to today's price.

Let's understand with an example.

Input:
prices = [100, 80, 60, 70, 60, 75, 85]


Expected spans:
[1, 1, 1, 2, 1, 4, 6]


2. Understand the output with a dry run
Day 1 – Price = 100

No previous day.

Span = 1

Day 2 – Price = 80

Previous price 100 is greater than 80.

Span = 1

Day 3 – Price = 60

Previous price 80 is greater than 60.

Span = 1

Day 4 – Price = 70
- Today's price = 70
- Previous price = 60 (smaller)
- Previous price = 80 (greater)
We count 70 and 60.

Span = 2

Day 5 – Price = 60

Previous price 70 is greater.

Span = 1

Day 6 – Price = 75

We count:
- 75 (today)
- 60 (Day 5)
- 70 (Day 4)
- 60 (Day 3)
Day 2 has price 80, which is greater than 75, so we stop.

Span = 4

Day 7 – Price = 85

We count all previous six days because all their prices are less than or equal to 85.

Span = 6

3. Which approach should we use?
We use a Monotonic Decreasing Stack.

Before coding, understand one important idea:

Instead of storing every previous day's price and checking them again, we maintain a stack.

Each stack element stores two values:
[price, span]


For example:

stack = [
    [100, 1],
    [80, 1],
    [70, 2]
]

Here:
- 100 has span 1.
- 80 has span 1.
- 70 has span 2.
We maintain prices in decreasing order from bottom to top.



Question 1. Why do we initialize span = 1?
Ans = To count today's price


Question 2. Why do we use self.stack[-1][0] <= price?
Ans = To check whether the top previous price can be included

Question 3. Why do we add previous_span instead of simply adding 1?
Ans = Because we want to count all the previous days that can be included in the span.

Remember this rule:

Span = Today's day + number of consecutive previous days whose prices are less than or equal to today's price.

Question 
========
stack = [
    [100, 1],
    [80, 1],
    [70, 2]
]


Today's price is 90.


What will be the new span?
Ans = 5

Calculation:
- Start span = 1
- Pop [70, 2]: span = 1 + 2 = 3
- Pop [80, 1]: span = 3 + 1 = 4
- Stop at 100 because 100 is greater than 90.


'''


stack = [[10,20],[30,40],[50,60]]
print(stack[-1][0])

'''
Step-by-Step Breakdown
=======================
• stack[-1] accesses the last element of the outer list, which is the sublist [50, 60].
• [0] then accesses the first element of that retrieved sublist, which is the integer 50.
'''

print("\n")


'''
901. Online Stock Span

'''


class StockSpanner:

    def __init__(self):
        self.stack = []  # Initialize an empty stack to store pairs of (price, span)
        

    def next(self, price: int) -> int:
        
        span=1  # Initialize the span for the current price
        
        # While the stack is not empty and the price at the top of the stack is less than or equal to the current price
        
        while self.stack and self.stack[-1][0] <= price:
            previous_price, previous_span = self.stack.pop()
            span += previous_span

        self.stack.append([price, span])

        return span



obj = StockSpanner()
print(obj.next(100))  # Output: 1
print(obj.next(80))   # Output: 1
print(obj.next(60))   # Output: 1
print(obj.next(70))   # Output: 2
print(obj.next(60))   # Output: 1
print(obj.next(75))   # Output: 4
print(obj.next(85))   # Output: 6
print(obj.next(90))   # Output: 7


















