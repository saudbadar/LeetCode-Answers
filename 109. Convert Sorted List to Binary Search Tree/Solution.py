class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        lst, node = [], head
        while(node):
            lst.append(node.val)
            node = node.next
        
        def recursion(tempLst):
            if(not tempLst):
                return(None)
            middle = len(tempLst) // 2
            node = TreeNode(tempLst[middle])
            node.left = recursion(tempLst[:middle])
            node.right = recursion(tempLst[middle + 1:])
            return(node)
        return(recursion(lst))