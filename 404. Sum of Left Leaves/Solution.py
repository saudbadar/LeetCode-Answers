class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def DFS(node, left):
            total = 0
            if(node.left):
                total += DFS(node.left, True)
            if(node.right):
                total += DFS(node.right, False)
            elif(not node.left and not node.right and left):
                total += node.val
            return(total)
        if(root):
            return(DFS(root, False))
        return(0)