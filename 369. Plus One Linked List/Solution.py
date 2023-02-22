class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        def recursive(node):
            carryOn = 0
            if(node.next):
                carryOn = recursive(node.next)
            else:
                if(node.val == 9):
                    node.val = 0
                    return(1)
                node.val += 1
                return(0)
            if(carryOn):
                if(node.val == 9):
                    node.val = 0
                    return(1)
                node.val += 1
                return(0)
            return(0)
        if(recursive(head)):
            return(ListNode(1, head))
        else:
            return(head)