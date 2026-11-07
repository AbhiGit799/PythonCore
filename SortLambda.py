'''

intervals.sort(key=lambda x: x[1])

Its purpose is to sort intervals based on their ending time (second element).

1. Understand the input
========================
intervals = [
    [1, 2],
    [2, 3],
    [3, 4],
    [1, 3]
]


Each interval has two values:
- x[0] → Starting time
- x[1] → Ending time

Example 
x = [1, 3]

x[0] = 1  # Start
x[1] = 3  # End

2. What does lambda x: x[1] mean?
===================================
A lambda is a small anonymous function.

This:

lambda x: x[1]

Equivalent to: 
def get_end_time(x):
    return x[1]

So whenever Python receives an interval, it returns its second value.

3. How does sorting work?
Consider:
intervals = [
    [1, 2],
    [2, 3],
    [3, 4],
    [1, 3]
]


Python checks the ending times:
Interval	x[1] (End time)
[1,2]	2
[2,3]	3
[3,4]	4
[1,3]	3

It sorts based on these ending times in ascending order.

Result:
[
    [1, 2],
    [2, 3],
    [1, 3],
    [3, 4]
]

4. What if we use x[0] instead?

intervals.sort(key=lambda x: x[0])


Now Python sorts based on starting time instead.

For example:

[
    [1, 2],
    [1, 3],
    [2, 3],
    [3, 4]
]


5. Remember this Python pattern
Code	Meaning
lambda x: x[0]	Sort by first element
lambda x: x[1]	Sort by second element
lambda x: x[1], reverse=True	Sort by second element descending

Why do we use x[1] in LeetCode 435?

Because our greedy strategy is to keep the interval that finishes earliest. Sorting by ending time makes that possible.



'''

intervals = [ [5,8], [1,4], [2,3], [3,5] ]

intervals.sort(key=lambda x:x[1])

print(intervals)


'''
In Python, key is a parameter of the sort() function that tells Python what value to use when sorting.

Think of it as: "On which basis should I sort?"

1. Without key

numbers = [5, 2, 8, 1]

numbers.sort()

print(numbers)

Output = [1, 2, 5, 8]

Python sorts numbers by their actual values.
2. With key
Consider:

intervals = [[5, 8], [1, 4], [3, 6]]

intervals.sort(key=lambda x: x[1])

Here:
- key tells Python which value to consider.
- lambda x: x[1] tells Python to consider the second element of each interval.


3. Can we use a normal function instead of lambda?
Yes!

'''
print("\n")

def get_end_time(x):
    return x[1]

intervals.sort(key=get_end_time)
print(intervals)


'''

Code	Meaning
sort()	Sort normally
sort(reverse=True)	Sort descending
sort(key=...)	Sort using a specific value
sort(key=lambda x: x[1])	Sort using the second element


'''
print("\n")

print(f"Previous start = {intervals[0][0]}")

print(f"Previous end = {intervals[0][1]}")

print("\n")

for i in range(len(intervals)):
    print(f"Interval {i}: Start = {intervals[i][0]}, End = {intervals[i][1]}")

print("\n")


for i in range(1,len(intervals)):
    print(f"Interval {i}: Start = {intervals[i][0]}, End = {intervals[i][1]}")














