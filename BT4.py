'''
1448. Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X 
there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:

      3
     / \
    1   4
   /   / \
  3   1   5

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.


1. Understand the problem
A node is called a good node if, on the path from the root to that node, there are no nodes with a value greater than the current node's value.
In simple words:
- Start from the root.
- Travel down to each node.
- If the current node's value is greater than or equal to every previous value on that path, it is a good node.


Let's check each node:

Node	Path from root	               Good?	           Why?

3	       3	                       Yes	               Root is always good
1	     3 → 1	                       No	               3 is greater than 1
4	     3 → 4	                       Yes	               4 ≥ 3
3	     3 → 1 → 3	                   Yes	               3 ≥ maximum value 3
1	     3 → 4 → 1	                   No	               3 and 4 are greater
5	     3 → 4 → 5	                   Yes	               5 ≥ maximum value 4


Answer: 4 good nodes.




'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if node is None:
                return 0

            count = 0

            if node.val >= maxVal:
                count = 1

            maxVal = max(maxVal, node.val)

            count += dfs(node.left, maxVal)
            count += dfs(node.right, maxVal)

            return count

        return dfs(root, root.val)


'''

7. Practice question

       5
      / \
     3   8
    / \   \
   4   2   7

How many good nodes are there?

Correct! There are 4 good nodes.
Good nodes are 5, 8, 4, and 7. Node 4 is good because the path is 5 → 3 → 4, and 4 is greater 
than both earlier values? Actually, 4 is less than 5, so it is not good. 
The correct good nodes are 5, 8, and 7, giving 3 good nodes.



'''

















