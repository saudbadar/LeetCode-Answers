class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def DFS(node, loop):
            nonlocal ret
            if(node.left):
                DFS(node.left, loop + 1)
            if(node.right):
                DFS(node.right, loop + 1)
            elif(not node.right and not node.left):
                ret = max(loop, ret)
        if(root):
            DFS(root, 1)
        return(ret)