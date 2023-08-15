# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1 = pointer1 = ListNode()
        head2 = pointer2 = ListNode()
        while(head):
            if(head.val < x):
                pointer1.next = ListNode(head.val)
                pointer1 = pointer1.next
            else:
                pointer2.next = ListNode(head.val)
                pointer2 = pointer2.next
            head = head.next
        pointer1.next = head2.next
        return(head1.next)