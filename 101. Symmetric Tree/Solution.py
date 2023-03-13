class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        symmetric = True
        
        def check(node1, node2):
            nonlocal symmetric
            if(not node1 and not node2):
                return()
            if((not node1 and node2) or (node1 and not node2) or (node1.val != node2.val)):
                symmetric = False
                return()
            check(node1.left, node2.right)
            if(symmetric == False):
                return()
            check(node1.right, node2.left)
            if(symmetric == False):
                return()
        check(root.left, root.right)
        return(symmetric)