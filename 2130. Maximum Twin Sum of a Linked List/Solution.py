class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev, slow, fast = None, head, head
        while(fast and fast.next):
            fast = fast.next.next
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode
        
        leftSide, rightSide, ret = prev, slow, 0
        while(rightSide):
            ret = max(leftSide.val + rightSide.val, ret)
            leftSide = leftSide.next
            rightSide = rightSide.next
        return(ret)