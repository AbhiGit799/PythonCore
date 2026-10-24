'''
735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.


'''


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = [];
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if stack[-1] < abs(a):
                    stack.pop()
                    continue;
                elif stack[-1] == abs(a):
                    stack.pop()
                break
            else:
                    stack.append(a)
        return stack;


        
asteroids = [5,10,-5]

obj = Solution()

print(obj.asteroidCollision(asteroids))

'''

5. What do abs() and pop() mean?
- abs(a) converts a negative number to its positive size. For example, abs(-5) = 5.
- stack.pop() removes the last asteroid from the stack.
- continue checks for another collision if the current asteroid survives the previous one.
- break stops checking collisions for the current asteroid.
Remember: Use a stack because the current asteroid may collide with the most recently added asteroid, and it might need to collide with earlier asteroids too.

'''



