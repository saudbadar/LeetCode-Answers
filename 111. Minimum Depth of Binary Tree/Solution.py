class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        if(root):
            queue.append((root, 0))

        while(queue):
            node, depth = queue.popleft()
            if(not node.left and not node.right):
                return(depth + 1)
            if(node.left):
                queue.append((node.left, depth + 1))
            if(node.right):
                queue.append((node.right, depth + 1))
        return(0)