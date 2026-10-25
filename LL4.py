'''
2130. Maximum Twin Sum of a Linked List

Let's understand this problem step by step using a simple example, then learn the Python solution.

1. What is the question asking?
You are given a linked list with an even number of nodes.

Two nodes are called twins when their positions add up to (n-1), using zero-based indexing.

In simple words:
- The first node is paired with the last node.
- The second node is paired with the second-last node.
- The third node is paired with the third-last node.
- Find the maximum sum among all these pairs.


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 


'''


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def printList(self,head):
        current = head
        
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
    
    def pairSum(self, head: ListNode | None) -> int:
        # Step 1: Find the middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev = None
        current = slow

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Step 3: Calculate maximum twin sum
        first = head
        second = prev
        max_sum = 0

        while second:
            total = first.val + second.val
            max_sum = max(max_sum, total)

            first = first.next
            second = second.next

        return max_sum



values = [5,4,2,1]
head = ListNode(values[0])
current = head

for value in values[1:]:
    current.next = ListNode(value)
    current = current.next 

obj = Solution()    

result = obj.pairSum(head)

print(result)


'''
3. What approach should we use?
Since you are learning linked lists and the fast/slow pointer technique, this problem is a good application of it.

We can solve it in three steps:
1. Find the middle using slow and fast pointers.
2. Reverse the second half of the linked list.
3. Compare both halves and calculate the maximum sum.

'''


