"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
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

def removeNthFromEnd_ver1(head, n):
    """
    :type head: Optional[ListNode]
    :type n: int
    :rtype: Optional[ListNode]
    """
    #print("input head = ", head, " n = ", n)
    sp = fp = head
    drift = 0

    while drift < n:
        if fp.next == None:
            #print("Breaking: ", fp, drift)
            break
        fp = fp.next
        drift += 1
    #print("Loop end: ", fp, drift)

    if drift < n:
        # not enough elements to drift, [1], n=1 case
        if sp == fp:
            return(None)
        else:
            return(sp.next)


    while fp.next != None:
        sp = sp.next
        fp = fp.next
    #print("End of second loop :", "sp = ", sp, "fp = ", fp)
    sp.next = sp.next.next
    return(head)

def removeNthFromEnd_ver2(head, n):
        res = ListNode(0, head)
        dummy = res

        for _ in range(n):
            head = head.next
        
        while head:
            head = head.next
            dummy = dummy.next
        
        dummy.next = dummy.next.next

        return res.next

if __name__ == "__main__":
    list1 = ListNode(1)
    list1.insert(2)
    list1.insert(3)
    list1.insert(4)
    list1.insert(5)    
    print_list(removeNthFromEnd_ver1(list1, 2))
    list1 = ListNode(1)
    list1.insert(2)
    list1.insert(3)
    list1.insert(4)
    list1.insert(5) 
    print_list(removeNthFromEnd_ver2(list1, 2))
    print("-----"*10)


    list2 = ListNode(1)
    print_list(removeNthFromEnd_ver1(list2, 1))
    list2 = ListNode(1)
    print_list(removeNthFromEnd_ver2(list2, 1))
    print("-----"*10)

    list3 = ListNode(1)
    list3.insert(2)
    print_list(removeNthFromEnd_ver1(list3, 1))
    list3 = ListNode(1)
    list3.insert(2)
    print_list(removeNthFromEnd_ver2(list3, 1))
    print("-----"*10)

    list4 = ListNode(1)
    list4.insert(2)
    print_list(removeNthFromEnd_ver1(list4, 2))
    list4 = ListNode(1)
    list4.insert(2)
    print_list(removeNthFromEnd_ver2(list4, 2))
    print("-----"*10)
