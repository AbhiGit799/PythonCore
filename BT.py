# 1. Understand the TreeNode class

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = TreeNode(10, TreeNode(5), TreeNode(15))

print(node.val)        # 10
print(node.left.val)   # 5
print(node.right.val)  # 15



# Think of TreeNode as a blueprint for creating one node in a binary tree.

'''

Example: a node whose value is 5 and which has no children yet.

- val stores the value inside the node.
- left stores a reference to the left child node.
- right stores a reference to the right child node.

Important: left and right usually store other TreeNode objects, not just integer values.


2. What happens when we create an object?

Let's create our first object.

root = TreeNode(5)

What happens here?
Python calls the constructor:

def __init__(self, val=0, left=None, right=None):

The value 5 is passed to val.
Because you didn't provide left or right, their default values are used.
So Python effectively performs these assignments:

self.val = 5
self.left = None
self.right = None

None means that the node currently has no child on that side.


3. How do we assign left and right children?
Suppose we want to build this binary tree:

      5
     / \
    3   8


We can create it using three objects.

root = TreeNode(5)
# Creates a node with value 5

root.left = TreeNode(3)
# Creates a new node with value 3 and stores that node's reference in root.left.



root.right = TreeNode(8)
# Creates another node with value 8 and stores its reference in root.right.

Now the tree is complete!
Notice that root.left does not contain just the integer 3. It refers to the entire node object created by TreeNode(3).

4. Can we create the whole tree in one line?
Yes! We can pass the left and right children directly to the constructor.

root = TreeNode(
    5,
    TreeNode(3),
    TreeNode(8)
)

Why does this work?
The constructor parameters are in this order:

TreeNode(val, left, right)


Therefore:
Argument	              Assigned to	          Value
First: 5	                   val	               5
Second: TreeNode(3)	          left	              A node containing 3
Third: TreeNode(8)	          right	              A node containing 8


The resulting tree is:

      5
     / \
    3   8



The two child nodes also have their own left and right attributes, which are None by default.

5. What if we pass all three arguments?
node = TreeNode(10, TreeNode(5), TreeNode(15))

This creates the following structure:

       10
      /  \
     5    15

Here is the key point:
- node.val gives 10.
- node.left.val gives 5.
- node.right.val gives 15.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node = TreeNode(10, TreeNode(5), TreeNode(15))

print(node.val)        # 10
print(node.left.val)   # 5
print(node.right.val)  # 15


6. What do self, val, left, and right mean?
Name	Meaning
self	The object currently being initialized
val	The value passed to the constructor
left	The left child provided to the constructor
right	The right child provided to the constructor
self.val	The value stored inside this object
self.left	The left child reference stored inside this object
self.right	The right child reference stored inside this object

For example:

node = TreeNode(7)

Inside __init__:

self.val = val

means: store 7 in the object's val attribute.

And:

self.left = left
self.right = right

means: store None in both child attributes because no children were supplied.


left and right store a reference to the child node object, not just the node's value.

       root
        10
       /  \
      5    20

What is stored in each attribute?
Expression	What it stores or returns
root.val	The integer 10
root.left	A reference to the TreeNode object containing 5
root.right	A reference to the TreeNode object containing 20
root.left.val	The integer 5
root.right.val	The integer 20

'''
























