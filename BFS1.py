
"""
199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

"""

from collections import deque;

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                if i == size-1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
        return result;


# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

root = TreeNode(1)
root.left=TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right=TreeNode(4)

obj = Solution()

result = obj.rightSideView(root)

print(result)


'''
Imagine standing on the right side of the tree. The visible nodes are:
- Level 0 → 1
- Level 1 → 3
- Level 2 → 4
Output: [1, 3, 4]

We need the rightmost node at each level.

Important Note
===============
Because BFS processes nodes from left to right, the last node processed at each level is the rightmost node.


Remember this pattern
- BFS → visits nodes level by level.
- Queue → manages the order of visiting nodes.
- size = len(queue) → identifies the current level's node count.
- i == size - 1 → identifies the last node of that level.
Interview takeaway: Whenever a tree problem asks for the first or last node at each level, think of BFS + level order traversal.


Note = popleft() removes and returns the first element from a queue in Python.


Remember:
- popleft() → removes from the beginning.
- append() → adds to the end.


queue = deque([root]) means create a queue and put the root node into it.


Remember:
- popleft() → removes from the beginning.
- append() → adds to the end.
This makes the queue work in FIFO order: First In, First Out.

Key Logic
**********
The logic used in LeetCode 199 is BFS (Breadth-First Search) + Level Order Traversal.

The main idea is simple: visit each level from left to right and store the last node of every level.




'''










