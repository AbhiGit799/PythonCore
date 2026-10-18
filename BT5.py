
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
        def isValidBST(self, root: TreeNode | None) -> bool:
             def dfs(node,low,high):
                  if node is None:
                       return True
                  if node.val<=low or node.val>=high:
                       return False
                  return(
                       dfs(node.left,low,node.val)
                       and
                       dfs(node.right,node.val,high)
                  )
             return dfs(root,float('-inf'),float('inf'))



root = TreeNode(2)
# root.left = TreeNode(100)
# root.right = TreeNode(31)

obj = Solution()

print(obj.isValidBST(root))

'''
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Input: root = [2,1,3]
Output: true

'''

# Important Note
'''
root = TreeNode(2)
obj = Solution()
print(obj.isValidBST(root))

Python creates this tree:

      2
     / \
   None None

Remember your TreeNode constructor:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


Because you passed only 2:
- root.val = 2
- root.left = None
- root.right = None
The tree contains only one node, with value 2. This is a valid BST.


Ex:2
======
      2
     / \
   100  31


This tree is not a valid BST, because:
- 100 is on the left of 2, but 100 > 2.
- 31 is on the right of 2, and 31 > 2, which is correct.

The left child violates the BST rule, so the answer should be False.


'''

# Note
'''

4. Remember these two cases

Code condition	                                  Meaning	                                                             Return
node is None	                                 No node exists here; nothing violates the rules	                      True
Node value is outside its allowed range	        BST rule is violated	                                                  False



The key takeaway: 

return True for None means “this part of the tree is valid because 
there is nothing here that can violate the rules.” 
It does not mean the entire tree has already been validated; 
DFS continues checking the other nodes.


1. What are float('-inf') and float('inf')?
In Python, they represent negative infinity and positive infinity.


float('-inf')  # Negative infinity: -∞
float('inf')   # Positive infinity: +∞

Think of them as values smaller or larger than every ordinary number.

float('-inf') < -1000000  # True
float('inf') > 1000000    # True


2. Why do we use them in Validate BST?
Remember our code:
return dfs(root, float('-inf'), float('inf'))

We call dfs() with three arguments:

dfs(node, low, high)


- node: The current node we are checking.
- low: The minimum allowed boundary.
- high: The maximum allowed boundary.
Initially, we haven't checked any nodes, so any integer value should be allowed for the root.

We therefore start with:

low  = -∞
high = +∞


Remember: 
==========
We use negative and positive infinity because we don't want to impose an arbitrary minimum or maximum value on the root. As we move down the tree, we narrow the allowed range based on each node's value.



'''


# Important Note
# ===============
'''

root = [10,5,15]

Step 1: Check root 10

dfs(10, -inf, inf)

10 is greater than negative infinity and less than positive infinity, so it is valid.


'''


'''

1. First, understand the parameters

node: The current node we are checking.

low: The minimum allowed boundary.

high: The maximum allowed boundary.



5. Compare the two calls

Direction	     Correct function call	                           Meaning
Left	        dfs(node.left, low, node.val)	                   Keep low; update high
Right	        dfs(node.right, node.val, high)	                   Update low; keep high


Easy trick to remember:
- Going left means values must be smaller, so update the upper limit (high).
- Going right means values must be greater, so update the lower limit (low).




'''








