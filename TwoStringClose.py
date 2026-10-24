'''
1657. Determine if Two Strings Are Close

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

'''


word1 = "abc"; word2 = "bca"

for i in word1:
    print(i)


print("\n")

for j in word2:
    print(j)

print("\n")



class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        if set(word1) != set(word2):
            return False
        
        freq1 = sorted(word1.count(ch) for ch in set(word1))
        freq2 = sorted(word2.count(ch) for ch in set(word2))

        return freq1 == freq2

obj = Solution()

word1 ="aabbcc" ; word2="abbccc"; 

print(obj.closeStrings(word1,word2))
print(obj.closeStrings("aab","abb"))

'''

The key idea

To determine whether two strings are close, two conditions must be satisfied.
- Condition 1: Same characters. Both strings must contain exactly the same set of distinct characters.
- Condition 2: Same frequency distribution. Both strings must have the same collection of character frequencies, 
  although those frequencies can belong to different characters.

For example:

word1 = "aabbcc" → frequencies [2, 2, 2]

word2 = "abbccc" → frequencies [1, 2, 3]

Both have the same characters, but their frequency distributions differ. Therefore, they are not close.



6. Why do we use set() and sorted()?
- set(word1) removes duplicate characters so we can compare which distinct characters exist.
- sorted() arranges the frequencies in order, allowing us to compare the frequency distributions regardless of which character has each frequency.
For example, [1, 3, 2] and [2, 1, 3] are different lists, but their sorted versions are equal: [1, 2, 3].


7. Time and space complexity
Let n be the length of the strings.
- Time complexity: O(n log n), mainly because of sorting the frequencies.
- Space complexity: O(n) in the general case, due to the sets and frequency lists.

'''
        




