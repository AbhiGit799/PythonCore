'''
1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

'''



class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = {}

        for num in arr:
            freq[num] = freq.get(num,0)+1
            print(freq[num])
            print(freq)

        counts=list(freq.values())

        return len(counts) == len(set(counts))
        


obj = Solution()

print(obj.uniqueOccurrences([1,1,1,2,2,3,]))


'''

Remember the approach
1. Use a dictionary to count each number.
2. Extract the frequency values.
3. Convert those values to a set.
4. Compare the lengths.
- Time complexity: \(O(n)\) on average.
- Space complexity: \(O(n)\).



2. Why do we convert it into a list?
Actually, we don't strictly need to convert it into a list for this problem. 
I used list() to make the frequency counts easier to understand as a normal list.

We can solve the problem without it:

This works because dict_values supports len() and can be passed to set().

'''


