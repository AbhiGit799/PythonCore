'''

LeetCode 236: Lowest Common Ancestor of a Binary Tree

Let's learn this problem step by step using a simple tree, then understand the Python recursion.

1. What is the question asking?
The Lowest Common Ancestor (LCA) of two nodes p and q is the lowest node in the tree that is an 
ancestor of both nodes.

A node can also be an ancestor of itself.


Suppose:
- p = 5
- q = 1
Their lowest common ancestor is node 3, because both nodes are below node 3, 
and neither node is an ancestor of the other.

Now suppose:
- p = 5
- q = 2

Their lowest common ancestor is node 5, because node 5 is itself an ancestor of node 2.


2. What approach should we use?
We'll use DFS (Depth-First Search) with recursion.

Think about the problem this way:
1. Search the left subtree.
2. Search the right subtree.
3. If p is found on one side and q on the other, the current node is their lowest common ancestor.

'''



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        if left:
            return left
        
        return right
        

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.right = TreeNode(2)
root.left.left = TreeNode(6)
root.right.right = TreeNode(8)
root.right.left = TreeNode(0)

obj = Solution()

p = root.left 
q = root.right

result = obj.lowestCommonAncestor(root,p,q)

print(result.val)


'''
       3
      / \
     5   1
    / \
   6   2
      / \
     7   4


We are given:
- p = 5
- q = 4


2. Trace the path to each node

Path to node 5:

3 → 5

Path to node 4:

3 → 5 → 2 → 4

Both paths share nodes 3 and 5.

Which shared node is the lowest (closest to the target nodes)?

It's node 5.

3. Why not node 2?

Node 2 is below node 5, but node 5 is not below node 2.

Node 2 is an ancestor of node 4, but it is not an ancestor of node 5.

Therefore, node 2 cannot be the common ancestor of both.

Remember: The Lowest Common Ancestor is the lowest node that is an ancestor of both target nodes. 
A target node can also be its own ancestor.

'''



