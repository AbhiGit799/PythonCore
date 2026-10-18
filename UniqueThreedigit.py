'''

LeetCode 3483 — Unique 3-Digit Even Numbers

Let's solve this in Python step by step, focusing on the approach and why it works.
This problem is a good exercise in arrays, loops, and permutations. We don't need recursion for this one.

1. Understand the problem
You are given a list of digits, digits. Your task is to count how many unique 3-digit even numbers you can form using those digits.
Remember three rules:
- The hundreds digit cannot be 0.
- The last digit must be even: 0, 2, 4, 6, or 8.
- You cannot use a digit more times than it appears in the input.


2. Python solution — three nested loops
We'll try every possible combination of three positions in the input array and store valid numbers in a set. A set automatically keeps only unique numbers.



'''

class Solution:
    def totalNumbers(self,digits:list[int])->int:
        numbers = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i==j or j==k or i==k:
                        continue

                    if digits[i]==0:
                        continue

                    if digits[k]%2!=0:
                        continue


                    number = digits[i]*100 + digits[j]*10+digits[k]

                    numbers.add(number)
        return len(numbers)


obj = Solution()

n = [1,2,3,4]

print(obj.totalNumbers(n))


'''

We need three digits, so we use three loops:
- i selects the hundreds digit.
- j selects the tens digit.
- k selects the units digit.


For example, if digits = [1, 2, 3, 4]:

Variable	Index	Digit
i	         0	     1
j	         1	     2
k	         3	     4


These positions form the number 124.




'''












