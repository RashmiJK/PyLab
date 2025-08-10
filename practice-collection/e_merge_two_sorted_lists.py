"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
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

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    list3 = ListNode()
    list3_ret = list3

    while list1 and list2:
        if list1.val <= list2.val:
            list3.next = list1
            list1 = list1.next
        else:
            list3.next = list2
            list2 = list2.next
        list3 = list3.next
    
    if list1:
        list3.next = list1
    else:
        list3.next = list2
    
    return list3_ret.next

def print_list(head):
    # Print the merged linked list
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    list1 = ListNode(1)
    list1.insert(2)
    list1.insert(4)
    print_list(list1)

    list2 = ListNode(1)
    list2.insert(3)
    list2.insert(4)
    print_list(list2)

    merged_list = mergeTwoLists(list1, list2)
    print_list(merged_list)

