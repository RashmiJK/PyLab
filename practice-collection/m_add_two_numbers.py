"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""
#Definition for singly-linked list.
class ListNode(object):
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

def print_list(head):
    # Print the merged linked list
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

def addTwoNumbers(list1, list2):
    result = ListNode()
    dummy = result

    total = carry = 0
    while list1 or list2 or carry:
        total = carry
        
        if list1:
            total += list1.val
            list1 = list1.next 

        if list2:
            total += list2.val
            list2 = list2.next 

        num = total % 10
        carry = total // 10
        result.next = ListNode(num)
        result = result.next
    return dummy.next

if __name__ == "__main__":
    list1 = ListNode(2)
    list1.insert(4)
    list1.insert(3)
    print_list(list1)

    list2 = ListNode(5)
    list2.insert(6)
    list2.insert(4)
    print_list(list2)

    print_list(addTwoNumbers(list1, list2))
    print("---"*15)
    list1 = ListNode(9)
    list1.insert(9)
    list1.insert(9)
    list1.insert(9)
    list1.insert(9)
    list1.insert(9)
    list1.insert(9)
    print_list(list1)

    list2 = ListNode(9)
    list2.insert(9)
    list2.insert(9)
    list2.insert(9)
    print_list(list2)

    print_list(addTwoNumbers(list1, list2))