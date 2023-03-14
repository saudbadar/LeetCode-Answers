class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ret = 0

        def recursion(node, total):
            nonlocal ret
            tempVal = total * 10 + node.val
            if(node.left):
                recursion(node.left, tempVal)
            if(node.right):
                recursion(node.right, tempVal)
            if(not node.left and not node.right):
                ret += tempVal

        if(root):
            recursion(root, 0)
        return(ret)