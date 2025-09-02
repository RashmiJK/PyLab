"""
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def insert(self, val):
        #if not self.val:
        #    self.val = val
        #    return
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

def rotateRight(head, k):
    """
    :type head: Optional[ListNode]
    :type k: int
    :rtype: Optional[ListNode]
    """
    if not head:
        return head
    
    length = 1
    dummy = head

    while dummy.next:
        dummy = dummy.next
        length += 1

    pos = k % length

    if pos == 0:
        return head

    current = head

    for _ in range(length - pos - 1):
        current = current.next

    new_head = current.next
    current.next = None
    dummy.next = head

    return new_head

if __name__ == "__main__":
    list1 = ListNode(1)
    list1.insert(2)
    list1.insert(3)
    list1.insert(4)
    list1.insert(5)
    print_list(list1)
    print_list(rotateRight(list1, 2))

    list2 = ListNode()
    list2.insert(2)
    list2.insert(3)
    print_list(list2)
    print_list(rotateRight(list2, 4))