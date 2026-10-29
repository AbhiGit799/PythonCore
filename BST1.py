'''
700. Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the 
subtree rooted with that node. If such a node does not exist, return null.

 

Example 1:


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]


'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None or root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left,val)
        return self.searchBST(root.right,val)
        


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)


obj = Solution()
result = obj.searchBST(root, 2)


print(result.val)        # 2
print(result.left.val)   # 1
print(result.right.val)  # 3


'''

1. What is the question asking?
You are given the root of a Binary Search Tree (BST) and a value val.

Your task is to find the node whose value equals val and return that node along with its entire subtree. If the value doesn't exist, return None.

Since 2 exists, return the subtree rooted at node 2:

    2
   / \
  1   3


2. How do we search?
Remember the BST rule:
- If val == root.val, we found the node.
- If val < root.val, search the left subtree.
- If val > root.val, search the right subtree.
- If the current node is None, the value doesn't exist.  



Time and space complexity
Let h be the height of the tree.
- Time: O(h), because we follow only one branch.
- Space: O(h) for the recursive call stack.
For a balanced BST, searching is typically O(log n). 
For a highly unbalanced BST, the worst case is O(n).



'''





