# 104. Maximum Depth of Binary Tree
'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2

'''


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val 
        self.left = left 
        self.right = right


class Solution:
    def maxDepth(self,root:TreeNode|None)->int:
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)  # Used Recursion
        right_depth = self.maxDepth(root.right)  # Used Recursion


        return 1+max(left_depth,right_depth)


obj = Solution()

# Input-1 root = [1,null,2]
print("\n")
root = TreeNode(1)
root.right = TreeNode(2)
print(obj.maxDepth(root))


'''
For Input-1 root = [1,null,2]

1 is the root.
None means the root has no left child.
2 is the right child of 1.


LeetCode represents a binary tree in level-order format 
(level by level, from left to right).

For Input-1 root = [10,20,30,40]

Position in list	Value	               Meaning
1st	                10	                    Root
2nd	               	20	               Left child of 10
3rd	               	30	               Right child of 10
4th	               	40	               Left child of 20

'''

    

'''

1. Understand the problem
You are given the root of a binary tree. Return its maximum depth.
Maximum depth means the number of nodes along the longest path from the root node down to any leaf node.

2. Think about the approach
Imagine you are standing at the root. You need to find the longest depth in its left subtree and its right subtree.
The logic is:
1. Find the maximum depth of the left subtree.
2. Find the maximum depth of the right subtree.
3. Take the larger depth.
4. Add 1 for the current node.


The formula is:
  
      depth = 1 + max(left depth,right depth)


But what happens when there is no node? That is our base case.
- If root is None, return 0.
- Otherwise, calculate the depths of its children and return 1 + max(left, right)

The reason we add 1 is that we must count the current node itself when calculating the maximum depth.

Ex => 

root = [1,2,3,4]

root = 1
left of root = 2
right of root = 3
left of 2 = 4

The longest path is:
1 → 2 → 4
How many nodes are there? 3 nodes, so the maximum depth is 3.


2. Calculate from the bottom upward
Let's start with node 4.
At node 4:
It has no children, so:

left_depth = 0
right_depth = 0

return 1 + max(0, 0)
# 1 + 0 = 1

Why 1? Because node 4 itself counts as one node.

At node 2:
Its left child has depth 1 (node 4), and its right child has depth 0.

return 1 + max(1, 0)
# 1 + 1 = 2

The depth of the subtree rooted at node 2 is 2.

At node 1:
Its left subtree has depth 2, and its right subtree has depth 1.

return 1 + max(2, 1)
# 1 + 2 = 3

The maximum depth is 3.




Quick practice
Suppose a tree contains only one node:
    10


What should its maximum depth be?
Ans = 1

A single node has depth 1. Its children are None, so 1 + max(0, 0) = 1.



'''























