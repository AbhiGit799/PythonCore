'''
872. Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



Input: 

root1 = [3,5,1,6,2,9,8,null,null,7,4], 
root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:

Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false


'''



class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val 
        self.left = left 
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def getLeaves(root):
            if root is None:
                return []

            if root.left is None and root.right is  None:
                return [root.val]

            return getLeaves(root.left)+getLeaves(root.right)

        return getLeaves(root1) == getLeaves(root2)

    def leafSimilar1(self, root1, root2):
        def getLeaves1(root):
            if root is None:
                return []

            if root.left is None and root.right is None:
                return [root.val]

            return getLeaves1(root.left) + getLeaves1(root.right)

        leaves1 = getLeaves1(root1)
        leaves2 = getLeaves1(root2)

        result = leaves1 == leaves2

        return result, leaves1, leaves2



# root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]

root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.right.left = TreeNode(9)
root1.right.right = TreeNode(8)

root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)

root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.right = TreeNode(1)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)

root2.right.right.left = TreeNode(9)
root2.right.right.right = TreeNode(8)

obj = Solution()
print(obj.leafSimilar(root1, root2))

print("\n")
print(obj.leafSimilar1(root1, root2))




















