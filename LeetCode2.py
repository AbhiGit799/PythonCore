# 345. Reverse Vowels of a String

'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


How it works

Strings are immutable in Python, so convert to a list of characters first.
Each iteration either skips a non-vowel on one side or swaps when both pointers sit on vowels.
A set gives O(1) vowel lookups, and including uppercase letters handles both cases.


'''



class Solution:
    def reverseVowels(self,s:str)->str:
        vowels = set('aeiouAEIOU')
        chars = list(s)
        left,right=0,len(chars)-1 
        while left<right:
            if chars[left] not in vowels:
                left=left+1
            elif chars[right] not in vowels:
                right=right-1
            else:
                chars[left],chars[right]=chars[right],chars[left]
                left=left+1
                right=right-1
        return ''.join(chars)


obj = Solution();

print(obj.reverseVowels("hello")) # Output: "holle"



'''

chars[left], chars[right] = chars[right], chars[left]

This line swaps the characters at positions left and right in the list. 
It uses Python's tuple packing and unpacking, so no temporary variable is needed.

What happens step by step

The right side, chars[right], chars[left], is evaluated first. Python builds a tuple holding the two current values, in that order.
The tuple is then unpacked into the left side: the first value goes into chars[left] and the second into chars[right].

Because the right side is fully evaluated before any assignment happens, neither value gets overwritten too early.

Example

Say chars = ['I', 'c', 'e', 'C', 'r', 'e', 'A', 'm'], with left = 0 and right = 6.

Right side evaluates to ('A', 'I'), which is (chars[6], chars[0]).
chars[0] becomes 'A'.
chars[6] becomes 'I'.

The list is now ['A', 'c', 'e', 'C', 'r', 'e', 'I', 'm'].

The equivalent in other languages

Without tuple unpacking, you would need a temporary variable:

python
temp = chars[left]
chars[left] = chars[right]
chars[right] = temp

The one-line version does the same thing and is the idiomatic way to swap in Python. It works for any two variables or list positions, for example a, b = b, a.



'''

