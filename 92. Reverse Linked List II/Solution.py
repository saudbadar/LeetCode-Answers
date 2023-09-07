# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur, pos, newHead = head, 1, ListNode(0, head)
        leftPos = newHead

        if(right == left):
            return(head)

        while(pos < left):
            leftPos, cur = cur, cur.next
            pos += 1
        startNode, prevNode = cur, None
        for i in range(right - left + 1):
            nextNode, cur.next, prevNode = cur.next, prevNode, cur
            cur = nextNode
        startNode.next, leftPos.next = nextNode, prevNode
        return(newHead.next)