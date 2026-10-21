'''
LeetCode 437 — Path Sum III

Since we're learning Binary Tree DSA from easy to hard, 
this problem is a great next step because it combines DFS (Depth-First Search), recursion, and prefix sum.


Difficulty: Medium · Topic: Binary Tree + DFS + Prefix Sum


1. Understand the problem

You are given a binary tree and a target sum. Find the number of paths where the sum of the node values equals targetSum.
Important rules:
- A path can start at any node, not just the root.
- A path must move from parent to child.
- You can stop at any node.
- You cannot move upward or jump between branches.


root = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
targetSum = 8

Three valid paths:
1. 5 → 3 = 8
2. 5 → 2 → 1 = 8
3. -3 → 11 = 8
Output: 3




'''



prefix = {0:10}    # Creates a dictionary where the integer 0 is the key mapped to the integer 10.

print(prefix[0])   

'''
Accesses the value using standard bracket indexing. 
It looks up key 0 and prints 10. 
If the key 0 did not exist, this would raise a KeyError.
'''

print(prefix.get(0))

'''
Uses the dictionary .get() method to look up key 0. It returns 10. 
If the key 0 were missing, it would return None instead of crashing.

'''

print(prefix.get(0,0)) # Output = 10

'''
Why is it 10 and not 0?

The .get(key, default) method works like this: if the key exists in the dictionary, it returns its actual value. 
It only uses the fallback default value if the key is missing.
Since the key 0 exists in your dictionary and is mapped to 10, Python returns 10 and completely ignores the fallback 0.

'''


'''

Approach 2 — Prefix Sum + DFS (optimized)
This is the more efficient approach, and it connects directly to the prefix sum concept you were learning.

First, understand prefix sum
Suppose a path contains these values:

10 → 5 → 3

The running sums are:

Node	Running sum
10	       10
5	       15
3	       18

The running sum at node 3 is 18.

If we want a path sum of 8, we can calculate:

Current Sum - Previous Sum = Target

Rearranging:

Previous Sum = Current Sum - Target

At node 3:
              18 - 8 = 10

              
The previous prefix sum 10 belongs to node 10. 
Subtracting it gives us the path 5 → 3, whose sum is 8.
This is the key idea: instead of checking every possible path separately, we use a dictionary to remember the prefix sums we've encountered.



'''

print("\n")


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        prefix = {0: 1}

        def dfs(node, curr_sum):
            if node is None:
                return 0

            curr_sum += node.val

            needed = curr_sum - targetSum
            count = prefix.get(needed, 0)

            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1

            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            prefix[curr_sum] -= 1

            return count

        return dfs(root, 0)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

obj = Solution()
target = 3
print(obj.pathSum(root,target))











