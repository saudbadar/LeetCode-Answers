class Solution:
    def __init__(self, head: Optional[ListNode]):
        node, self.lst = head, []
        while(node):
            self.lst.append(node.val)
            node = node.next
        

    def getRandom(self) -> int:
        return(random.choice(self.lst))