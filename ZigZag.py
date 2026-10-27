'''
1372. Longest ZigZag Path in a Binary Tree

You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        self.ans=0
        def dfs(node,left,right):
            if not node:
                return
            self.ans = max(self.ans,left,right)
            dfs(node.left,right+1,0)
            dfs(node.right,0,left+1)
        dfs(root,0,0)
        return self.ans
        


# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(3)

# Call the function
obj = Solution()
result = obj.longestZigZag(root)

print(result)

'''

1. What is the question asking?

A ZigZag path means you must alternate directions at every step:
- Left
- Right
- Left
- Right
Or the opposite:
- Right
- Left
- Right
- Left
You cannot go left twice in a row or right twice in a row.

Important: The path can start at any node in the tree.

2. Example ExTree.png

Consider the path:

1 → 2 → 5
- From node 1 to node 2: move Left.
- From node 2 to node 5: move Right.
This is a ZigZag path with 2 edges.

Notice that we count edges, not nodes. So three nodes connected by two edges give a path length of 2.


3. What approach should we use?
We'll use DFS (Depth-First Search) + Recursion.

The idea is simple:
1. Start at the root.
2. Try moving left and right.
3. If the direction alternates, increase the ZigZag length by 1.
4. If the same direction repeats, reset that path's length to 0.
5. Keep track of the maximum length found.


'''