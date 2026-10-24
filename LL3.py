'''
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.


'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

    def printList(self,head):
        current = head
        
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

'''
next_node = current.next  # Save next node
current.next = prev       # Reverse the link
prev = current            # Move prev forward
current = next_node       # Move current forward

'''

values = [1,2,3,4,5]

head = ListNode(values[0])

current = head

for value in values[1:]:
    current.next = ListNode(value)
    current = current.next 

obj = Solution()

obj.printList(head)

result = obj.reverseList(head)

obj.printList(result)


'''

Remember: head = ListNode(values[0]) is important because it creates the starting node and gives us a reference 
to the beginning of the linked list. Without head, you would not have an easy way to access the complete list 
from its first node.


'''
