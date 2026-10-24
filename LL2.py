    # def printList(self,head):
    #     current = head
        
    #     while current:
    #         print(current.val, end=" -> ")
    #         current = current.next
    # print("None")




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self, head):
        current = head

        while current:
            print(current.val, end=" -> ")
            current = current.next

        print("None")

    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenHead
        return head


values = [1, 2, 3, 4, 5]

head = ListNode(values[0])
current = head

for value in values[1:]:
    current.next = ListNode(value)
    current = current.next

obj = ListNode()
result = obj.oddEvenList(head)

obj.printList(result)


# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]




