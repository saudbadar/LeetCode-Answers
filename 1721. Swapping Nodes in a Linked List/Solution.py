class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        loc, leftSide, val = head, head, 0
        while(loc):
            val += 1
            if(val == k):
                leftSide = loc
            loc = loc.next
        newLoc, loc = val - k, head
        for i in range(newLoc):
            loc = loc.next
        loc.val, leftSide.val = leftSide.val, loc.val
        return(head)