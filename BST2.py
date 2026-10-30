'''

450. Delete Node in a BST


Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.

Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left,key)

        elif key>root.val:
            root.right = self.deleteNode(root.right,key)

        else:
            # Case 1: No left child
            if root.left is None:
                return root.right

            # Case 2: No right child
            if root.right is None:
                return root.left

            # Case 3: Two Children
            successor = root.right

            while successor.left:
                successor = successor.left
            root.val = successor.val

            root.right = self.deleteNode(root.right,successor.val)
        
        return root 
        




'''

1. What is the question asking?
********************************
You are given a Binary Search Tree (root) and a value (key).

Your task is to:
1. Find the node whose value equals key.
2. Delete that node.
3. Return the updated root of the BST.
Remember the BST rule:
- Left subtree values are smaller than the node.
- Right subtree values are greater than the node.

2. The three cases you must understand
*****************************************
Case 1: The node has no children (leaf node)
Easy: just remove the node. The parent no longer points to it.

Case 2: The node has one child
The child takes the deleted node's place.

Case 3: The node has two children
This is the most important case.

Solution: Find the smallest value in the right subtree.
- Right subtree of 4 contains 6, 5, 7.
- The smallest value is 5.
- Replace 4 with 5.
- Delete the original node 5 from the right subtree.

This replacement value is called the inorder successor.
                                     ******************
Ex: BT = [4,2,6,1,3,5,7]
Node to delete is = 4

Now the BT = looks like

        5
       / \
      2   6
     / \   \
    1   3   7


Time Complexity = O(h) where h is the height of the BST.
Recursive space = O(h)


Good question! The reason we traverse the right subtree is related to the BST rule. Let's understand it with a simple example.

1. Consider this BST

        8
       / \
      4   12
         /  \
        10   14


Suppose we want to delete node 8.

Node 8 has two children: 4 and 12.

We need to find a replacement value for 8 without breaking the BST rules.

2. Why find the smallest value in the right subtree?
Remember the BST rule:
- Left subtree values must be smaller than the node.
- Right subtree values must be greater than the node.
After deleting 8, its replacement must fit between the values on its left and right.


The values in the right subtree are 10, 12, 14.

The smallest value is 10.

Why is 10 a good replacement?
- 4 < 10 — the left subtree is still smaller.
- 10 < 12 and 10 < 14 — the remaining right-subtree values are greater.
So we can safely replace 8 with 10.


3. What if we traverse the left subtree instead?
The left subtree contains 4.

If we replace 8 with 4, we get a problem: the original left child is also 4, creating a duplicate, and the original right subtree contains values greater than 8.

We could instead use the largest value in the left subtree as the replacement. This is called the inorder predecessor.


        8                  4
       / \                / \
      4   12     →       ?   12
         /  \
        10   14



 The correct predecessor approach would replace 8 with the largest value from its left subtree, then remove that original node from the left subtree. It works too.


 4. Remember this rule

There are two valid ways to delete a node with two children:

Approach	Where to search	Name
Method 1	Go right, then as far left as possible	Inorder successor
Method 2	Go left, then as far right as possible	Inorder predecessor

LeetCode solutions commonly use Method 1, which is why we find the smallest value in the right subtree.

The key idea: We don't have to choose the right subtree. We can choose either method, as long as we preserve the BST ordering and remove the original replacement node correctly.



Yes! ✅ Method 1 (inorder successor) works for all three deletion cases in LeetCode 450, when implemented correctly.

But remember, Method 1 is specifically used when the node has two children.

How it handles all cases
Case	Situation	         What to do
1	    No children	         Return None
2	    One child	         Replace the node with its child
3	   Two children	         Find the smallest value in the right subtree, replace the node's value, and delete the original successor




Example of Case 3

       8
      / \
     4   12
        /  \
       10   14

Delete 8:
1. Find the smallest value in the right subtree → 10.
2. Replace 8 with 10.
3. Delete the original 10 node

       10
      /  \
     4    12
            \
             14

Notice that the original 10 is removed, and the BST ordering remains valid.
-


Remember: You don't need to use the inorder predecessor as well. Using the inorder successor consistently is sufficient for this problem.


'''


'''

Let's understand Inorder Successor and Inorder Predecessor in a Binary Search Tree (BST) with simple examples.

1. First, understand the meaning
Imagine the BST values are sorted in ascending order:

2, 4, 6, 8, 10, 12, 14

If we choose node 8:
- Inorder Successor: the next larger value → 10
- Inorder Predecessor: the next smaller value → 6
Think of reading a sorted list:
- Successor = next value.
- Predecessor = previous value.

2. Inorder Successor
The inorder successor is the smallest value greater than the current node.

Rule when the node has a right subtree:
1. Go to the right child.
2. Keep moving left until you cannot go left anymore.
For node 8:
- Go right → 12
- Go left → 10
- No more left child → successor is 10.



3. Inorder Predecessor
The inorder predecessor is the largest value smaller than the current node.

Using the same tree, find the predecessor of 8.

Rule when the node has a left subtree:
1. Go to the left child.
2. Keep moving right until you cannot go right anymore.
For node 8:
- Go left → 4
- Go right → 6
- No more right child → predecessor is 6.


4. Compare both rules

Successor
==========
Right → Left → Left...

Find the smallest value in the right subtree.

Example: successor of 8 is 10.

Predecessor
============
Left → Right → Right...

Find the largest value in the left subtree.

Example: predecessor of 8 is 6.


5. What if the node has no right or left subtree?
This is an important detail: the rules above work when the respective subtree exists.
- If there is no right subtree, finding the successor may require moving up through the ancestors until you find a node where you came from its left side.
- If there is no left subtree, finding the predecessor may require moving up until you find a node where you came from its right side.
- If no such ancestor exists, that successor or predecessor does not exist.
For example, in a BST containing 2, 4, 6, 8, the successor of 8 does not exist because 8 is the largest value.





'''














