'''
1. What is Backtracking?

Backtracking is a problem-solving technique where:
1. We make a choice.
2. We explore what happens after that choice.
3. If we reach a solution, we save it.
4. We go back and undo our previous choice.
5. We try another choice.

In simple words:
==================
Backtracking means trying different possibilities, one by one, by choosing, exploring, and undoing choices.


2. Real-life example
Imagine you are standing in front of a maze.

You need to reach the destination.

What will you do?
- Start walking on one path.
- If the path reaches the destination, you succeed.
- If the path is blocked, go back.
- Try another path.
- Continue until you find the destination.
This is exactly how Backtracking works.



3. Understand Backtracking with a simple Python example
Suppose you have three choices:


choices = ["A", "B", "C"]

You want to generate all possible selections containing exactly two letters.

Expected output:

[
    ["A", "B"],
    ["A", "C"],
    ["B", "C"]
]

Let's solve this using Backtracking.

Python code

def backtrack(start, current):

    if len(current) == 2:
        result.append(current.copy())
        return

    for i in range(start, len(choices)):

        # 1. Choose
        current.append(choices[i])

        # 2. Explore
        backtrack(i + 1, current)

        # 3. Undo the choice
        current.pop()


choices = ["A", "B", "C"]

result = []

backtrack(0, [])

print(result)

O/P => [['A', 'B'], ['A', 'C'], ['B', 'C']]

4. Understand the three important operations

Look at these three lines:

current.append(choices[i])

backtrack(i + 1, current)

current.pop()

These are the heart of Backtracking.
Operation	          Meaning
append()	         Make a choice
backtrack()	         Explore further
pop()	             Undo the choice


7. Why do we use current.copy() instead of current?
**************************************************
This is another important Python concept.

We write:
result.append(current.copy())

Why not:
result.append(current)


Because Python lists are mutable.

If we save current directly, future append() and pop() operations will modify the same list stored in result.

current.copy() creates a separate copy so our saved combination does not change.

8. Backtracking vs Recursion vs DFS
************************************
These concepts are related, but they are not the same.


Concept	             Meaning
Recursion	         A function calls itself
DFS	                 Explore one path deeply before exploring another
Backtracking	     Make a choice, explore it, then undo it to try another choice

Backtracking commonly uses recursion and DFS.


Pattern
=========

def backtrack():

    # 1. Check base condition

    # 2. Explore available choices
    for choice in choices:

        # 3. Make a choice
        current.append(choice)

        # 4. Explore further
        backtrack()

        # 5. Undo the choice
        current.pop()


This is the basic Backtracking template. The exact loop and recursive arguments change depending on the problem.



'''




'''

17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) 
is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

















'''

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        current = []

        def backtrack(index):

            if index == len(digits):
                result.append("".join(current))
                return

            digit = digits[index]

            for letter in phone[digit]:

                current.append(letter)

                backtrack(index + 1)

                current.pop()

        backtrack(0)

        return result


obj = Solution()
digits = "23"
print(obj.letterCombinations(digits))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]



print("\n\n\n")

def backtrack(start, current):

    if len(current) == 2:
        result.append(current.copy())
        return

    for i in range(start, len(choices)):

        # 1. Choose
        current.append(choices[i])

        # 2. Explore
        backtrack(i + 1, current)

        # 3. Undo the choice
        current.pop()


choices = ["A", "B", "C"]

result = []

backtrack(0, [])

print(result)

















