''''

'''


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = "aeiou"
        count = 0;
        for i in range(k):
            if s[i] in vowel:
                count = count+1
        max_count = count

        # Slide the window
        for i in range(k, len(s)):
            # Remove the character leaving the window
            if s[i - k] in vowel:
                count -= 1

            # Add the character entering the window
            if s[i] in vowel:
                count += 1

            max_count = max(max_count, count)

        return max_count


obj = Solution()

s = "abciiidef"; k = 3

print(obj.maxVowels(s,k))


'''

Why subtract 1? Because the new window no longer contains "a".
If the outgoing character were "b", we would not subtract anything because "b" is not a vowel.





'''
        

