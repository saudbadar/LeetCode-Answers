class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head or not head.next):
            return(head)
        ret, prev, current = ListNode(0, head), head, head.next
        shift = ret
        while(prev and current):
            prev.next, current.next, shift.next = current.next, prev, current
            if(prev.next):
                shift, current, prev = prev, prev.next.next, prev.next
            else:
                break
        return(ret.next)