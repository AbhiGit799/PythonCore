'''

1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.


        1          Level 1 → Sum = 1
       / \
      7   0        Level 2 → Sum = 7 + 0 = 7
     / \
    7  -8           Level 3 → Sum = 7 + (-8) = -1

    

The sums are:
Level	Sum
1	     1
2	     7
3	    -1

Remember: the question asks for the level number, not the maximum sum itself. Level numbering starts from 1.

'''

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        queue = deque([root])
        level=1
        max_sum = float('-inf')
        answer=1

        while queue:
            size = len(queue)
            current_sum=0
            for i in range(size):
                node = queue.popleft()
                current_sum = current_sum + node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if current_sum > max_sum:
                max_sum = current_sum
                answer = level

            level = level+1
        
        return answer
        

'''
Input: root = [1,7,0,7,-8,null,null]
Output: 2
'''

root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(0)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)

obj = Solution()

print(obj.maxLevelSum(root))







