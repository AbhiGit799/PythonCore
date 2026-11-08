'''

Binary Search in DSA – Beginner-Friendly Explanation
Binary Search is one of the most important searching algorithms in DSA. It is frequently asked in LeetCode interviews.


1. What is Binary Search?
Binary Search is an algorithm that finds an element by repeatedly dividing the search space into two halves.

Instead of checking every element one by one, we check the middle element and decide which half we should search next.

Let's take this sorted array:


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]


Suppose we need to find 70.

We could check every element one by one, but Binary Search is faster.
2. How does Binary Search work?
We maintain three variables:
- left – starting index.
- right – ending index.
- mid – middle index.
Initially:

left = 0
right = len(arr) - 1

Step 1: Find the middle index

mid = (left + right) // 2

mid = (0 + 8) // 2
mid = 4

arr[mid] = 50

We want 70, but the middle element is 50.

Since 70 > 50, we know our target must be on the right side.

We can eliminate:

10, 20, 30, 40, 50

Update:
left = mid + 1


def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]

print(binary_search(arr, 70))


'''





'''
374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1


'''

pick = 6

def guess(num):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:

        left = 1
        right = n

        while left <= right:

            mid = left + (right - left) // 2

            result = guess(mid)

            if result == 0:
                return mid

            elif result == -1:
                right = mid - 1

            else:
                left = mid + 1


solution = Solution()
print(solution.guessNumber(10))


'''
Understand the question
You are given a number n.

The system secretly selects a number between 1 and n.

You need to guess that number.

There is a predefined API:

guess(num)

It returns one of three values:
Return value	Meaning
-1	            Your guess is higher than the actual number
1	            Your guess is lower than the actual number
0	            Your guess is correct


Ex:

n = 10
pick = 6


You need to find the secret number 6.

Suppose you guess:
- Guess 5 → Returns 1 (your guess is too low).
- Guess 8 → Returns -1 (your guess is too high).
- Guess 6 → Returns 0 (correct!).


2. Which approach should we use?
We use Binary Search.

Why?

Because every time we guess a number, we get information about whether the actual number is higher or lower.

Instead of checking every number one by one, we eliminate half of the search space.



'''




'''

mid = left + (right - left) // 2

3. Then why do we use the second formula?

The main reason is Integer Overflow.

Imagine you're using a programming language like Java, C++ or C.

These languages have a maximum value that an integer can store.

Suppose we have

left = 2_000_000_000
right = 2_100_000_000


with traditional formula:
mid = (left + right) // 2


The addition become:

2,000,000,000 + 2,100,000,000
= 4,100,000,000

This exceeds the maximum value of a signed 32-bit integer (2,147,483,647).

It can cause integer overflow in languages using 32-bit integers.

The alternative formula avoids that large addition:

mid = left + (right - left) // 2

Both formulas give the same middle index when there is no overflow.

The second formula is preferred mainly for overflow safety, not because it produces a different Binary Search result.


'''











