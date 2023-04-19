class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def dfs(node, depth, leftLast):
            nonlocal ret
            depthRight, depthLeft = 1, 1
            ret = max(ret, depth)
            if(node.right):
                if(leftLast):
                    depthRight = depth + 1
                dfs(node.right, depthRight, False)
            if(node.left):
                if(not leftLast):
                    depthLeft = depth + 1
                dfs(node.left, depthLeft, True)
        if(root.left):
            dfs(root.left, 1, True)
        if(root.right):
            dfs(root.right, 1, False)
        return(ret)