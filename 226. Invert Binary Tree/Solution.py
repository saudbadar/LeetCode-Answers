class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def DFS(node):
            if(node.left):
                DFS(node.left)
            if(node.right):
                DFS(node.right)
            node.left, node.right = node.right, node.left
            
        if(root):
            DFS(root)
        return(root)