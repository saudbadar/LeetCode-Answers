class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        

    def getRandom(self) -> int:
        scope, ret, cur = 1, 0, self.head
        while(cur):
            if(random.random() < (1 / scope)):
                ret = cur.val
            cur = cur.next
            scope += 1
        return(ret)