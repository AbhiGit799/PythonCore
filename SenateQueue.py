'''
In Python, if senate is a string (str), calling enumerate(senate) 
will break the string down into individual characters. 
It returns an iterable enumerate object yielding pairs of (index, character).
'''

senate = "Senate"
# Convert to a list to see the pairs immediately
print(list(enumerate(senate)))

'''
output
[(0, 'S'), (1, 'e'), (2, 'n'), (3, 'a'), (4, 't'), (5, 'e')]

💡 Common Use Case
You will most frequently use this in a for loop to track both the position and the character at the same time:

'''
for index, char in enumerate(senate):
    print(f"Character at index {index} is '{char}'")

from collections import deque

class Solution:
    def predictVictory(self,senate:str)->str:
        radiant = deque()
        dire = deque()
        n = len(senate)

        for i,ch in enumerate(senate):
            if ch=="R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(r+n)
            else:
                dire.append(d+n)

        return "Radiant" if radiant else "Dire"



obj = Solution()

print(obj.predictVictory("RDD"))








