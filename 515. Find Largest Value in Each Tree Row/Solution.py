# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        
        def DFS(node, depth):
            if(len(lst) <= depth):
                lst.append(node.val)
            else:
                lst[depth] = max(lst[depth], node.val)
            if(node.left):
                DFS(node.left, depth + 1)
            if(node.right):
                DFS(node.right, depth + 1)
        if(root):
            DFS(root, 0)
        return(lst)

