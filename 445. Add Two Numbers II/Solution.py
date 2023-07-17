# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        amountOne, amountTwo = 0, 0
        
        while(l1 != None):
            amountOne = (amountOne * 10) + l1.val
            l1 = l1.next
        while(l2 != None):
            amountTwo = (amountTwo * 10) + l2.val
            l2 = l2.next
        
        dummylist = dummy = ListNode(0)
        for i in str(amountOne + amountTwo):
            dummy.next = ListNode(i)
            dummy = dummy.next
        
        return(dummylist.next)