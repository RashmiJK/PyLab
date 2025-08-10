"""
Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

# Singly linked list
class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def insert(self, val):
        if not self.val:
            self.val = val
            return
        if not self.next:
            self.next = ListNode(val)
            return
        current = self
        while current.next:
            current = current.next
        current.next = ListNode(val)

    def print_list(self):
        current = self
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

def deleteDuplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


if __name__ == "__main__":
    list1 = ListNode(1)
    list1.insert(1)
    list1.insert(1)
    list1.insert(2)
    list1.insert(3)
    list1.insert(3)
    list1.print_list()

    deleteDuplicates(list1)

    list1.print_list()
