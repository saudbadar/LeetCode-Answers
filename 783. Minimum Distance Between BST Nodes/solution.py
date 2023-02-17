class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        minVal = sys.maxsize
        def DFS(node, lower, upper):
            nonlocal minVal
            minVal = min(upper - node.val, node.val - lower, minVal)
            if(node.left):
                DFS(node.left, lower, node.val)
            if(node.right):
                DFS(node.right, node.val, upper)

        DFS(root, float('-inf'), float('inf'))
        return(minVal)